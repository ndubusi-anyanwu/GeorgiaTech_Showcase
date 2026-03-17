package edu.gatech.battle.user;

import java.util.List;

import lombok.Data;

@Data
public class PaginatedUserDto {
    private List<User> users; // List of users
    private long totalCount; // Total count of users

    public PaginatedUserDto(List<User> users, long totalCount) {
        this.users = users;
        this.totalCount = totalCount;
    }
}
