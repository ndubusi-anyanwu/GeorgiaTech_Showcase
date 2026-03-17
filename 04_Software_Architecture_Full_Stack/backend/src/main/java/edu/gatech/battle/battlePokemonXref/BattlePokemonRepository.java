package edu.gatech.battle.battlePokemonXref;

import org.springframework.data.repository.CrudRepository;
import org.springframework.data.repository.PagingAndSortingRepository;

public interface BattlePokemonRepository extends CrudRepository<BattlePokemon, Long>, PagingAndSortingRepository<BattlePokemon, Long> {
}
