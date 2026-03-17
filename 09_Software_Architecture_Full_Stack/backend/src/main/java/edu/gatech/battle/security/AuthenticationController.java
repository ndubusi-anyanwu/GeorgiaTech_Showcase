package edu.gatech.battle.security;

import java.util.HashMap;
import java.util.Map;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.security.authentication.AuthenticationManager;
import org.springframework.security.authentication.UsernamePasswordAuthenticationToken;
import org.springframework.security.core.Authentication;
import org.springframework.validation.annotation.Validated;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import edu.gatech.battle.Response;
import edu.gatech.battle.user.UserService;
import jakarta.validation.Valid;

@Validated
@RestController
@RequestMapping("/api/auth")
public class AuthenticationController {

    @Autowired
    private UserService userService;
    @Autowired
    private JwtService jwtService;
    @Autowired
    private AuthenticationManager authenticationManager;

    // register a new user
    @PostMapping("/register")
    public ResponseEntity<Response> register(@RequestBody @Valid RegistrationRequest registrationRequest) {
        Response response = userService.register(registrationRequest);
        return new ResponseEntity<>(response, HttpStatus.CREATED);
    }

    // login a user
    @PostMapping("/login")
    public ResponseEntity<Map<String, String>> login(@RequestBody LoginRequest loginRequest) {
        Authentication authentication = authenticationManager.authenticate(
                new UsernamePasswordAuthenticationToken(loginRequest.getUsername(), loginRequest.getPassword()));

        String token = jwtService.generateToken(authentication.getName());
        String refreshToken = jwtService.generateRefreshToken(authentication.getName());
        String userRole = userService.getUserRole(loginRequest.getUsername());
        Map<String, String> tokens = new HashMap<>();
        tokens.put("accessToken", token);
        tokens.put("refreshToken", refreshToken);
        tokens.put("userRole", userRole);
        return new ResponseEntity<>(tokens, HttpStatus.OK);
    }

    @PostMapping("/refresh-token")
    public ResponseEntity<?> refreshToken(@RequestBody Map<String, String> tokenRequest) {
        String refreshToken = tokenRequest.get("refreshToken");

        try {
            // Validate the refresh token
            String username = jwtService.extractUsername(refreshToken);
            if (username == null || !username.isEmpty()) {
                return ResponseEntity.status(HttpStatus.UNAUTHORIZED).body("Invalid username");
            }
            // Generate new tokens
            String newAccessToken = jwtService.generateToken(username);
            String newRefreshToken = jwtService.generateRefreshToken(username);

            Map<String, String> tokens = new HashMap<>();
            tokens.put("accessToken", newAccessToken);
            tokens.put("refreshToken", newRefreshToken);

            return ResponseEntity.ok(tokens);
        } catch (Exception e) {
            return ResponseEntity.status(HttpStatus.UNAUTHORIZED).body("Invalid refresh token");
        }
    }
}
