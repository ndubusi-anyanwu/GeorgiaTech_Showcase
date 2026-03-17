package edu.gatech.battle.user;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.security.access.prepost.PreAuthorize;
import org.springframework.validation.annotation.Validated;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

import edu.gatech.battle.Response;

@Validated
@RestController
@RequestMapping("/api/user")
public class UserController {

    @Autowired
    private UserService userService;

    @GetMapping("/roles")
    @PreAuthorize("hasAnyRole('ROLE_USER', 'ROLE_ADMIN', 'ROLE_TRAINER')")
    public ResponseEntity<List<Role>> getRoles() {
        List<Role> roles = userService.getRoles();
        if (roles == null) {
            return ResponseEntity.notFound().build();
        }
        return new ResponseEntity<>(roles, HttpStatus.OK);
    }

    @GetMapping("/get")
    @PreAuthorize("hasRole('ROLE_ADMIN')")
    public ResponseEntity<PaginatedUserDto> getUsers(@RequestParam(defaultValue = "0") int page,
            @RequestParam(defaultValue = "10") int size) {
        PaginatedUserDto users = userService.getUsers(page, size);
        return new ResponseEntity<>(users, HttpStatus.OK);
    }

    @GetMapping("/updateRole")
    @PreAuthorize("hasRole('ROLE_ADMIN')")
    public ResponseEntity<Response> updateRole(@RequestParam Long userId, @RequestParam int roleId) {
        return new ResponseEntity<>(userService.updateRole(userId, roleId), HttpStatus.OK);
    }

    @GetMapping("/delete")
    @PreAuthorize("hasRole('ROLE_ADMIN')")
    public ResponseEntity<Response> delete(@RequestParam Long userId) {
        return new ResponseEntity<>(userService.delete(userId), HttpStatus.OK);
    }
}
