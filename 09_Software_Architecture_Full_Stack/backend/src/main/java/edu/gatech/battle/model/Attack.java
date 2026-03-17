package edu.gatech.battle.model;

import jakarta.persistence.Entity;
import lombok.Data;

@Entity
@Data
public class Attack extends Skill {

    private final Boolean type = false;
    private Integer damage;
}
