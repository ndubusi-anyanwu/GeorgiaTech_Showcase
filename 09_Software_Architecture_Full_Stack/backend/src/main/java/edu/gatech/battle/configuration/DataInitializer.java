package edu.gatech.battle.configuration;

import java.util.Map;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.CommandLineRunner;
import org.springframework.stereotype.Component;

import edu.gatech.battle.user.Role;
import edu.gatech.battle.user.RoleRepository;
import edu.gatech.battle.user.User;
import edu.gatech.battle.user.UserRepository;

@Component
public class DataInitializer implements CommandLineRunner {

    @Autowired
    private RoleRepository roleRepository;
    @Autowired
    private UserRepository userRepository;

    @Override
    public void run(String... args) throws Exception {
        Map<String, Integer> rolesWithIds = Map.of(
                "USER", 1,
                "TRAINER", 2,
                "ADMIN", 3);

        for (Map.Entry<String, Integer> entry : rolesWithIds.entrySet()) {
            String roleName = entry.getKey();
            Integer roleId = entry.getValue();

            if (roleRepository.findByName(roleName).isEmpty()) {
                Role role = new Role();
                role.setId(roleId); // Set the ID explicitly
                role.setName(roleName);
                roleRepository.save(role);
                System.out.println("Inserted role: " + roleName + " with ID: " + roleId);
            }
        }

        // insert admin user
        Role adminRole = new Role();
        adminRole.setId(3);
        adminRole.setName("ADMIN");
        User adminUser = new User("admin_user", "$2a$10$lwdDZdRr5gQIghdWphMSVumwigdgUfTk.pLdxMkBY9fhy3Wlc00NW", "admin_user@pokemon.com", adminRole);
        adminUser.setFirstName("Admin");
        adminUser.setLastName("User");
        userRepository.save(adminUser);
        System.out.println("Inserted Admin User.");
    }
}