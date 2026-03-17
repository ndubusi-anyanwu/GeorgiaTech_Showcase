package edu.gatech.battle.battle;

import java.util.ArrayList;
import java.util.List;

import edu.gatech.battle.battlePokemonXref.BattlePokemon;
import edu.gatech.battle.battlePokemonXref.BattlePokemonService;
import edu.gatech.battle.item.Item;
import edu.gatech.battle.item.ItemService;
import edu.gatech.battle.pokemon.PokemonSummaryDto;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import edu.gatech.battle.pokemon.PokemonService;

@Service
public class BattleService {
    @Autowired
    private BattleRepository battleRepository;
    @Autowired
    private PokemonService pokemonService;
    @Autowired
    private BattlePokemonService battlePokemonService;
    @Autowired
    private ItemService itemService;

    public Battle init(BattleRequest request) {
        List<Item> items = itemService.getAllItems(0);

        List<BattlePokemon> pokemon = request.getPokemon().stream()
                .map(pokemonRequest -> {
                    BattlePokemon p = battlePokemonService.findById(pokemonRequest.getId(), pokemonRequest.isShouldInit());
                    p.setTemperature(pokemonRequest.getTemperature());
                    p.setItem(items);
                    return p;
                })
                .toList();
        Battle battle = new Battle(pokemon, request.getSeed(), request.getMaxTurns(), request.getBackground());
        battleRepository.save(battle);
        return battle;
    }

    public BattleDto getBattle(Long id) {
        Battle battle = battleRepository.findById(id).orElse(null);
        if (battle == null) {
            System.out.println("Battle not found");
            return null;
        }

        BattleDto dto = new BattleDto(battle);
        dto.setBattles(battle.execute());
        dto.getPokemon().values().forEach(pokemon -> pokemon.setSpriteUrl(pokemonService.getSprite(pokemon.getName())));

        // Save the entire battle so we store wins for participating Pokémon
        battleRepository.save(battle);

        return dto;
    }

    public List<PokemonSummaryDto> getPokemonThatCanBattle() {
        List<PokemonSummaryDto> pokemonList = new ArrayList<>();

        battlePokemonService.getPokemonList(0).forEach(p -> pokemonList.add(new PokemonSummaryDto(p)));
        pokemonService.getPokemonList(0).forEach(p -> pokemonList.add(new PokemonSummaryDto(p)));

        return pokemonList;
    }
}
