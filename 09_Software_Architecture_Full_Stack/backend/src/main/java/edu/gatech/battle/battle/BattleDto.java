package edu.gatech.battle.battle;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

import edu.gatech.battle.pokemon.PokemonDto;
import lombok.Data;

@Data
public class BattleDto {
    Long id;

    /**
     * Mapping of battlePokémon ID to Pokémon
     */
    Map<Long, PokemonDto> pokemon;

    List<BattleResult> battles;

    Boolean isTournament;

    String background;

    BattleDto (Battle battle) {
        this.id = battle.getId();
        this.pokemon = new HashMap<>();
        battle.getPokemon().forEach(battlePokemon -> pokemon.put(battlePokemon.getId(), new PokemonDto(battlePokemon.getPokemon())));
        this.isTournament = battle.getPokemon().size() > 2;
        this.battles = new ArrayList<>();
        this.background = battle.getBackground();
    }
}
