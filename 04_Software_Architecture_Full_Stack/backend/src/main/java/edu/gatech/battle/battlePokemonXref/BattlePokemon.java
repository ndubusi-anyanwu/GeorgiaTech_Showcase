package edu.gatech.battle.battlePokemonXref;

import edu.gatech.battle.model.Attack;
import edu.gatech.battle.model.Defense;
import edu.gatech.battle.model.Skill;
import edu.gatech.battle.model.Temp;
import edu.gatech.battle.pokemon.Pokemon;
import edu.gatech.battle.item.Item;
import jakarta.persistence.*;
import lombok.Data;

import java.util.List;
import java.util.Random;

@Entity
@Data
@Table(name="\"battle_pokemon\"")
public class BattlePokemon {

    @Id
    @GeneratedValue(strategy=GenerationType.AUTO)
    private Long id;

    @ManyToOne
    private Pokemon pokemon;

    private Integer wins = 0;
    private Integer seed;
    private Temp temperature;

    @ManyToOne
    @JoinColumn(name = "item_id")
    private Item item;

    // Transient fields, only used for battle logic
    @Transient
    private Integer currHp;

    @Transient
    private Skill latestTurn;

    @Transient
    private Random random;

    @Transient
    private boolean isItemUsed;

    public BattlePokemon() {
        this.random = new Random();
    }

    /**
     * Returns the BattlePokémon's name.
     */
    public String getName() {
        return this.pokemon.getName();
    }

    /**
     * Initializes the Pokémon for battle by resetting health.
     */
    public void prepare() {
        this.currHp = this.pokemon.getHp();
        this.latestTurn = null;
    }

    /**
     * Randomly sets an item from the provided list of items.
     * @param items A list of Item objects to choose from.
     * @return The selected item.
     */
    public Item setItem(List<Item> items) {
        if (this.item == null && items != null && !items.isEmpty()) {
            this.item = items.get(random.nextInt(items.size()));
        }
        return this.item;
    }

    /**
     * Randomly selects a skill based on the Pokémon's current health.
     * @return An attack or defense skill.
     */
    public Skill turnDecision() {
        int moveIndex;

        List<Attack> attackSkills = this.pokemon.getAttackSkills();
        List<Defense> defenseSkills = this.pokemon.getDefenseSkills();

        // Aggressive Skill Selection
        if (passesThreshold(new double[] {0.4, 0.7, 0.9})) {
            if (random.nextInt(9) > 1) {
                moveIndex = random.nextInt(attackSkills.size());
                latestTurn = attackSkills.get(moveIndex);
            } else {
                moveIndex = random.nextInt(defenseSkills.size());
                latestTurn = defenseSkills.get(moveIndex);
            }
        }
        // Balanced Skill Selection
        else if (passesThreshold(new double[] {0.15, 0.3, 0.65})) {
            if (random.nextInt(9) > 4) {
                moveIndex = random.nextInt(attackSkills.size());
                latestTurn = attackSkills.get(moveIndex);
            } else {
                moveIndex = random.nextInt(defenseSkills.size());
                latestTurn = defenseSkills.get(moveIndex);
            }
        }
        // Defensive Skill Selection
        else {
            if (random.nextInt(9) > 6) {
                moveIndex = random.nextInt(attackSkills.size());
                latestTurn = attackSkills.get(moveIndex);
            } else {
                moveIndex = random.nextInt(defenseSkills.size());
                latestTurn = defenseSkills.get(moveIndex);
            }
        }
        return latestTurn;
    }

    /**
     * Reduces current HP by the amount of provided damage, down to a minimum of 0.
     * If the Pokémon's latest turn was a defense skill, then the damage will be reduced.
     * @param damage The amount of damage to take.
     * @return Whether the Pokémon successfully reduced damage with a defense skill.
     */
    public boolean takeDamage(Integer damage) {
        boolean didReduce = false;
        if (latestTurn instanceof Defense) {
            didReduce = true;
            damage -= ((Defense) latestTurn).getDamageReduction();
            damage = Math.max(damage, 0);
        }
        currHp -= damage;
        currHp = Math.max(currHp, 0);
        return didReduce;
    }

    /**
     * Handles item usage if the Pokémon's HP is below half.
     * @return True if an item was successfully used, false otherwise.
     */
    public boolean useItemIfApplicable() {
        if (this.currHp <= this.pokemon.getHp() / 2 && (this.item.isReusable() || !this.isItemUsed())) {
            if (random.nextInt(100) < 50) { // 50% chance to use the item
                this.currHp += this.item.getValue(); // Restore HP
                this.currHp = Math.min(this.currHp, this.pokemon.getHp()); // Cap HP at max

                // If the item is not reusable, set it to null after use
                if (!this.item.isReusable()) {
                    this.setItemUsed(true);
                }
                return true;
            }
        }
        return false;
    }

    /**
     * Increases the Pokémon's number of wins.
     * @param didWin Whether the Pokémon won.
     * @return The Pokémon's number of wins.
     */
    public Integer setDidWin(boolean didWin) {
        if (didWin) wins++;
        return wins;
    }

    /**
     * Checks whether the Pokémon's HP ratio is greater than or equal to the provided threshold.
     * @param thresholds An array of three doubles, indexed by Temp.
     * @return Whether the Pokémon's HP passes the threshold for its current aggression temperature.
     */
    private boolean passesThreshold(double[] thresholds) {
        return (double) currHp / this.pokemon.getHp() >= thresholds[this.temperature.ordinal()];
    }
}
