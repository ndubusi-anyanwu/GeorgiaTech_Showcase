package edu.gatech.battle;

import edu.gatech.battle.item.ItemService;
import edu.gatech.battle.pokemon.PokemonService;
import org.springframework.boot.CommandLineRunner;
import org.springframework.stereotype.Component;

@Component
public class PokemonInitialization implements CommandLineRunner {
    private final PokemonService pokemonService;
    private final ItemService itemService;

    public PokemonInitialization(PokemonService pokemonService, ItemService itemService) {
        this.pokemonService = pokemonService;
        this.itemService = itemService;
    }

    @Override
    public void run(String... args) throws Exception {
        pokemonService.initPokemonData();
        itemService.initItemData();
    }
}
