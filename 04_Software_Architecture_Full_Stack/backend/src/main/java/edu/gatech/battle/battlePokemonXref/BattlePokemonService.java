package edu.gatech.battle.battlePokemonXref;

import edu.gatech.battle.item.Item;
import edu.gatech.battle.item.ItemRepository;
import edu.gatech.battle.pokemon.PokemonService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.data.domain.PageRequest;
import org.springframework.data.domain.Pageable;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
public class BattlePokemonService {

    @Autowired
    private BattlePokemonRepository pokemonRepository;

    @Autowired
    private PokemonService pokemonService;

    /**
     * Returns a battle Pokémon for the given ID, and can optionally initialize a new battle Pokémon.
     * @param id The ID if the Pokémon. If shouldInit is true, the ID corresponds to a template Pokémon.
     * @param shouldInit Whether a new battle Pokémon should be created.
     * @return The battle Pokémon.
     */
    public BattlePokemon findById(Long id, boolean shouldInit) {
        if (shouldInit) {
            BattlePokemon battlePokemon = new BattlePokemon();
            battlePokemon.setPokemon(pokemonService.findById(id));
            return pokemonRepository.save(battlePokemon);
        }
        return pokemonRepository.findById(id).orElse(null);
    }

    public List<BattlePokemon> getPokemonList(int page) {
        Pageable pageable = PageRequest.of(page, 48);
        return pokemonRepository.findAll(pageable).toList();
    }
}
