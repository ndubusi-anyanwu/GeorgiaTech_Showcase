package edu.gatech.battle.pokemon;

import edu.gatech.battle.model.Attack;
import edu.gatech.battle.model.Defense;
import edu.gatech.battle.model.Type;
import lombok.Data;

import java.util.List;

@Data
public class PokemonDto {
    private Long id;
    private String name;
    private List<Type> types;
    private List<Type> weaknesses;
    private List<Attack> attackSkills;
    private List<Defense> defenseSkills;
    private String spriteUrl;

    // Stats - not used for battle
    private Integer hp;
    private Integer attack;
    private Integer defense;
    private Integer specialAttack;
    private Integer specialDefense;
    private Integer speed;
    private Integer critRate;
    private Float height;
    private Float weight;
    private String category;
    private String abilities;
    private Integer gender;

    public PokemonDto(Pokemon pokemon) {
        this.id = pokemon.getId();
        this.name = pokemon.getName();
        this.types = pokemon.getTypes();
        this.weaknesses = pokemon.getWeaknesses();
        this.attackSkills = pokemon.getAttackSkills();
        this.defenseSkills = pokemon.getDefenseSkills();
        this.hp = pokemon.getHp();
        this.attack = pokemon.getAttack();
        this.defense = pokemon.getDefense();
        this.speed = pokemon.getSpeed();
        this.critRate = pokemon.getCritRate();
        this.specialAttack = pokemon.getSpecialAttack();
        this.specialDefense = pokemon.getSpecialDefense();
        this.height = pokemon.getHeight();
        this.weight = pokemon.getWeight();
        this.category = pokemon.getCategory();
        this.abilities = pokemon.getAbilities();
        this.gender = pokemon.getGender();
    }
}
