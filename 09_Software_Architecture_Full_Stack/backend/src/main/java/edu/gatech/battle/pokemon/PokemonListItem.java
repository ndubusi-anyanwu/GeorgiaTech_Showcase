package edu.gatech.battle.pokemon;

import lombok.Data;

@Data
public class PokemonListItem {

    private Long id;
    private String name;

    public PokemonListItem(Pokemon pokemon) {
        this.id = pokemon.getId();
        this.name = pokemon.getName();
    }
}
