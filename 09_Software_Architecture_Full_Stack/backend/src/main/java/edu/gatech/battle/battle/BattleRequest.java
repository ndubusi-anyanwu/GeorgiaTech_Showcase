package edu.gatech.battle.battle;

import edu.gatech.battle.battlePokemonXref.BattlePokemonRequest;
import lombok.Data;

import java.util.List;

@Data
public class BattleRequest {
    List<BattlePokemonRequest> pokemon;
    Integer seed;
    Integer maxTurns;
    String background;
}
