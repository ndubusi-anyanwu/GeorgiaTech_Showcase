package edu.gatech.battle.battle;

import edu.gatech.battle.battlePokemonXref.BattlePokemon;
import edu.gatech.battle.item.Item;
import edu.gatech.battle.model.Attack;
import edu.gatech.battle.model.Defense;
import edu.gatech.battle.model.Skill;
import jakarta.persistence.*;
import lombok.Data;

import java.util.ArrayList;
import java.util.List;
import java.util.Objects;

@Entity
@Data
@Table(name = "\"battle\"")
public class Battle {

    @Id
    @GeneratedValue(strategy = GenerationType.AUTO)
    private Long id;

    @ManyToMany
    @JoinTable(
            name = "battle_pokemon_xref",
            joinColumns = @JoinColumn(name = "battle_id"),
            inverseJoinColumns = @JoinColumn(name = "pokemon_id")
    )
    private List<BattlePokemon> pokemon = new ArrayList<>();

    private Integer seed = null;
    private Integer maxTurns = Integer.MAX_VALUE;
    private String background;

    public Battle() {}

    public Battle(List<BattlePokemon> pokemon, Integer seed, Integer maxTurns, String background) {
        this.pokemon = pokemon;
        this.seed = seed;
        if (maxTurns != null && maxTurns > 0) {
            this.maxTurns = maxTurns;
        }
        this.background = background;
    }

    /**
     * Executes a battle or tournament with all Pokémon, splitting them into battles of two as needed.
     * @return The result of the battle(s).
     */
    public List<BattleResult> execute() {
        if (this.pokemon.size() > 2) {
            return runTournament();
        }

        List<BattleResult> battleResults = new ArrayList<>();
        battleResults.add(runBattle(this.pokemon.get(0), this.pokemon.get(1)));
        return battleResults;
    }

    private List<BattleResult> runTournament() {
        List<BattleResult> results = new ArrayList<>();
        Integer round = 0;

        List<BattlePokemon> participants = this.pokemon;
        List<BattlePokemon> winners;
        do {
            winners = new ArrayList<>();
            for (int i = 0; i < participants.size() - 1; i += 2) {
                round++;
                BattleResult result = runBattle(participants.get(i), participants.get(i + 1));
                result.getComments().addFirst(String.format("Starting tournament round %d with %s and %s", round, participants.get(i).getName(), participants.get(i + 1).getName()));
                BattlePokemon winner = this.pokemon
                        .stream()
                        .filter(p -> Objects.equals(p.getId(), result.getWinner()))
                        .findFirst()
                        .orElseThrow();
                winners.add(winner);
                result.getComments().add(String.format("%s has won round %d", winner.getName(), round));
                results.add(result);
            }

            if (participants.size() % 2 == 1) {
                winners.addLast(participants.getLast());
            }

            participants = winners;
        } while (winners.size() > 1);

        return results;
    }

    private BattleResult runBattle(BattlePokemon x, BattlePokemon y) {
        BattleResult result = new BattleResult();

        x.prepare();
        y.prepare();

        if (this.seed != null) {
            x.setSeed(this.seed);
            y.setSeed(this.seed + 1);
        }

        int turnCount = 0;
        List<String> comments = new ArrayList<>();

        while (x.getCurrHp() > 0 && y.getCurrHp() > 0 && turnCount < this.maxTurns) {
            comments.addAll(this.takeTurn(x, y));
            turnCount++;
        }

        result.setComments(comments);
        battleEnd(result, x.getCurrHp() > 0 ? x : y, x.getCurrHp() > 0 ? y : x);

        return result;
    }

    private List<String> takeTurn(BattlePokemon x, BattlePokemon y) {
        List<String> comments = new ArrayList<>();

        comments.addAll(makeTurnDecision(x, y));

        if (y.getCurrHp() > 0) {
            comments.addAll(makeTurnDecision(y, x));
        }

        return comments;
    }

    private List<String> makeTurnDecision(BattlePokemon curr, BattlePokemon opponent) {
        List<String> comments = new ArrayList<>();

        if (curr.useItemIfApplicable()) {
            comments.add(String.format("%s used %s and restored some HP!", curr.getName(), curr.getItem().getName()));
        }

        Skill skill = curr.turnDecision();
        if (skill instanceof Attack attack) {
            comments.add(String.format("%s is attacking with %s for %d damage to %s", curr.getName(), attack.getName(), attack.getDamage(), opponent.getName()));
            boolean opponentDidDefend = opponent.takeDamage(attack.getDamage());
            if (opponentDidDefend) {
                Defense defense = (Defense) opponent.getLatestTurn();
                comments.add(String.format("%s successfully reduced %s's damage by %d with %s", opponent.getName(), curr.getName(), defense.getDamageReduction(), defense.getName()));
                int damageTaken = Math.max(attack.getDamage() - defense.getDamageReduction(), 0);
                comments.add(String.format("%s has received %d damage, remaining hp is %d", opponent.getName(), damageTaken, opponent.getCurrHp()));
            } else {
                comments.add(String.format("%s has received %d damage, remaining hp is %d", opponent.getName(), attack.getDamage(), opponent.getCurrHp()));
            }
        } else {
            comments.add(String.format("%s is attempting to defend with %s", curr.getName(), skill.getName()));
        }

        return comments;
    }


    private void battleEnd(BattleResult result, BattlePokemon winner, BattlePokemon loser) {
        winner.setDidWin(true);
        loser.setDidWin(false);
        result.setResult(winner, loser);
    }
}
