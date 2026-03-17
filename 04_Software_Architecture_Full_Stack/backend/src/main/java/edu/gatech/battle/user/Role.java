package edu.gatech.battle.user;

import jakarta.persistence.Column;
import jakarta.persistence.Entity;
import jakarta.persistence.Id;
import jakarta.persistence.Table;
import lombok.Data;

@Entity
@Table(name = "roles")
@Data
public class Role {  
    @Id
    private Integer id;
    @Column(nullable = false, unique = true)
    private String name;
}
