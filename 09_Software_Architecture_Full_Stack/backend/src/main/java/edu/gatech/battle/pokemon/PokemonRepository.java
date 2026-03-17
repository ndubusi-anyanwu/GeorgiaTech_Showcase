package edu.gatech.battle.pokemon;

import org.springframework.data.repository.CrudRepository;
import org.springframework.data.repository.PagingAndSortingRepository;

public interface PokemonRepository extends CrudRepository<Pokemon, Long>, PagingAndSortingRepository<Pokemon, Long> { }
