package edu.gatech.battle.user;

import java.util.List;
import java.util.Optional;

import org.mindrot.jbcrypt.BCrypt;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.data.domain.PageRequest;
import org.springframework.data.domain.Pageable;
import org.springframework.security.crypto.bcrypt.BCryptPasswordEncoder;
import org.springframework.stereotype.Service;

import edu.gatech.battle.Response;
import edu.gatech.battle.security.RegistrationRequest;
import edu.gatech.battle.security.UserContext;

@Service
public class UserService {
    @Autowired
    private UserRepository userRepository;
    @Autowired
    private RoleRepository roleRepository;
    @Autowired
    private BCryptPasswordEncoder passwordEncoder;

    // Save a new user or update an existing user
    public Response register(RegistrationRequest registrationRequest) {
        Optional<User> existingUser = userRepository.findByEmail(registrationRequest.getEmail());
        if (existingUser.isPresent()) {
            Response response = new Response("User already exists in the system.", false);
            return response;
        }

        Optional<User> existingUsername = userRepository.findByUsername(registrationRequest.getUsername());
        if (existingUsername.isPresent()) {
            Response response = new Response("Username is not available.", false);
            return response;
        }

        Role role = roleRepository.findByName("USER")
                .orElseThrow(() -> new RuntimeException("Default role USER not found"));

        // Hash the password using BCrypt
        String hashedPassword = passwordEncoder.encode(registrationRequest.getPassword());

        User user = new User(registrationRequest.getUsername(), hashedPassword, registrationRequest.getEmail(),
                role);
        user.setFirstName(registrationRequest.getFirstName());
        user.setLastName(registrationRequest.getLastName());

        userRepository.save(user);

        Response response = new Response("User registered successfully.", true);
        return response;
    }

    // Login a user by checking the email and hashed password
    public Response login(String username, String plainPassword) {
        // Retrieve the user by username
        Optional<User> existingUser = userRepository.findByUsername(username);
        if (existingUser.isEmpty()) {
            return new Response("User not found", false);
        }

        User user = existingUser.get();

        // Check if the provided password matches the stored hashed password
        if (BCrypt.checkpw(plainPassword, user.getPasswordHash())) {
            return new Response("Login successful", true);
        } else {
            return new Response("Invalid credentials", false);
        }
    }

    public List<Role> getRoles() {
        List<Role> roles = (List<Role>) roleRepository.findAll();
        if (roles.isEmpty()) {
            return null;
        }
        return roles;
    }

    public PaginatedUserDto getUsers(int page, int size) {
        Pageable pageable = PageRequest.of(page, size);
        String currentUsername = UserContext.getUsername();
        List<User> users = userRepository.findAllByIsActive(true, currentUsername, pageable);
        long totalUserCount = userRepository.countByIsActiveAndUsernameNot(true, currentUsername);
        PaginatedUserDto paginatedUserDto = new PaginatedUserDto(users, totalUserCount);
        return paginatedUserDto;
    }

    public Response updateRole(Long id, int roleId) {
        User user = userRepository.findById(id).orElseThrow(() -> new RuntimeException("User not found"));

        Role newRole = roleRepository.findById(roleId)
                .orElseThrow(() -> new RuntimeException("Role not found with ID: " + id));

        user.setRole(newRole);
        userRepository.save(user);
        Response response = new Response("User role updated successfully.", true);
        return response;
    }

    public Response delete(Long id) {
        if (!userRepository.existsById(id)) {
            throw new RuntimeException("User not found with ID: " + id);
        }
        userRepository.deleteById(id);
        Response response = new Response("User deleted successfully.", true);
        return response;
    }

    public String getUserRole(String username) {
        Optional<User> existingUser = userRepository.findByUsername(username);
        if (existingUser.isEmpty()) {
            return "";
        }
        User user = existingUser.get();
        return user.getRole().getName();
    }
}
