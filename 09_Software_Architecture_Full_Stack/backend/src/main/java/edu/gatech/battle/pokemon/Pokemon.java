package edu.gatech.battle.pokemon;

import edu.gatech.battle.battle.Battle;
import edu.gatech.battle.model.*;
import jakarta.persistence.*;
import lombok.Data;

import java.util.List;
import java.util.Random;

@Entity
@Data
@Table(name = "\"pokemon\"")
public class Pokemon {

  @Id
  @GeneratedValue(strategy=GenerationType.AUTO)
  private Long id;
  @Column(unique = true)
  private String name;
  @ElementCollection
  private List<Type> types;
  @ElementCollection
  private List<Type> weaknesses;
  @ManyToMany(cascade=CascadeType.ALL)
  private List<Attack> attackSkills;
  @ManyToMany(cascade=CascadeType.ALL)
  private List<Defense> defenseSkills;

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

  public Pokemon() {}
}