package edu.gatech.battle.battle;

import edu.gatech.battle.battlePokemonXref.BattlePokemon;
import lombok.Data;

import java.util.ArrayList;
import java.util.List;

@Data
public class BattleResult {

    private Long winner;
    private Long loser;

    private List<String> comments;

    BattleResult() {
        comments = new ArrayList<>();
    }

    public void setResult(BattlePokemon winner, BattlePokemon loser) {
        this.winner = winner.getId();
        this.loser = loser.getId();
        this.comments.add(loser.getName() + " has lost");
        this.comments.add(winner.getName() + " has won the battle");
    }
}
