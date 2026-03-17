package edu.gatech.battle.security;

public class UserContext {
    private static final ThreadLocal<String> username = new ThreadLocal<>();

    public static void setUsername(String id) {
        username.set(id); // Set the username in the current thread
    }

    public static String getUsername() {
        return username.get(); // Retrieve the username for the current thread
    }

    public static void clear() {
        username.remove(); // Clear the username for the current thread
    }
}