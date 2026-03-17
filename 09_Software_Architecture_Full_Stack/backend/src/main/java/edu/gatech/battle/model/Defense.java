package edu.gatech.battle.model;

import jakarta.persistence.Entity;
import lombok.Data;

@Entity
@Data
public class Defense extends Skill {

    private final Boolean type = true;
    private Integer damageReduction;
}
