package edu.gatech.battle.item;

import org.springframework.data.repository.CrudRepository;
import org.springframework.data.repository.PagingAndSortingRepository;
import org.springframework.stereotype.Repository;

@Repository
public interface ItemRepository extends CrudRepository<Item, Long>, PagingAndSortingRepository<Item, Long> {
    boolean existsByName(String name);
}
