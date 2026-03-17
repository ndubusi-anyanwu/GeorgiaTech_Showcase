package edu.gatech.battle.security;

import jakarta.validation.constraints.NotBlank;
import jakarta.validation.constraints.Size;

public class LoginRequest {

    @NotBlank(message = "Username is required")
    @Size(max = 50, message = "Username cannot be longer than 50 characters")
    private String username;
    public String getUsername() {
        return username;
    }

    @NotBlank(message = "Password is required")
    @Size(min = 8, max = 100, message = "Password must be between 8 and 100 characters")
    private String password;
    public String getPassword() {
        return password;
    }
}
