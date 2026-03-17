package edu.gatech.battle.battlePokemonXref;

import edu.gatech.battle.model.Temp;
import lombok.Data;

@Data
public class BattlePokemonRequest {
    private Long id;
    /**
     * True when a new BattlePokémon needs to be created
     */
    private boolean shouldInit;
    private Temp temperature;
}
