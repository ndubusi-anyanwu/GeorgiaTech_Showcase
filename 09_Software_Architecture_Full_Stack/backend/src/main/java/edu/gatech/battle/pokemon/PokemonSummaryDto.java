package edu.gatech.battle.pokemon;

import edu.gatech.battle.battlePokemonXref.BattlePokemon;
import lombok.Data;

@Data
public class PokemonSummaryDto {

    private Long id;
    private boolean isTemplate;
    private String name;
    private int wins;

    public PokemonSummaryDto(PokemonListItem pokemon) {
        this.id = pokemon.getId();
        this.name = pokemon.getName();
        this.isTemplate = true;
        this.wins = 0;
    }

    public PokemonSummaryDto(BattlePokemon battlePokemon) {
        this.id = battlePokemon.getId();
        this.name = battlePokemon.getName();
        this.isTemplate = false;
        this.wins = battlePokemon.getWins();
    }
}
