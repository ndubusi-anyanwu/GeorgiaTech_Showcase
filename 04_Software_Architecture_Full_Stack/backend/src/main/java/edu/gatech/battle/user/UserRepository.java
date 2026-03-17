package edu.gatech.battle.user;

import java.util.List;
import java.util.Optional;

import org.springframework.data.domain.Pageable;
import org.springframework.data.jpa.repository.Query;
import org.springframework.data.repository.CrudRepository;
import org.springframework.data.repository.PagingAndSortingRepository;
import org.springframework.data.repository.query.Param;

public interface UserRepository extends CrudRepository<User, Long>, PagingAndSortingRepository<User, Long> {

    // Custom query method to find a user by email
    Optional<User> findByEmail(String email);

    // Custom query method to find a user by username
    Optional<User> findByUsername(String username);

    @Query("SELECT u FROM User u WHERE u.isActive = :isActive and u.username != :username")
    List<User> findAllByIsActive(@Param("isActive") Boolean isActive, @Param("username") String username,
            Pageable pageable);

    long countByIsActiveAndUsernameNot(Boolean isActive, String username);
}
