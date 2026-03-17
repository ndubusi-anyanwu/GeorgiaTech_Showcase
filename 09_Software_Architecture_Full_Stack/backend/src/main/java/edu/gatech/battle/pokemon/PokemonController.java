package edu.gatech.battle.pokemon;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.security.access.prepost.PreAuthorize;
import org.springframework.validation.annotation.Validated;
import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

@Validated
@RestController
@RequestMapping("/pokemon")
@CrossOrigin(origins = "http://localhost:3001")
public class PokemonController {

    @Autowired
    private PokemonRepository pokemonRepository;
    @Autowired
    private PokemonService pokemonService;

    @GetMapping()
     @PreAuthorize("hasAnyRole('ROLE_USER', 'ROLE_ADMIN', 'ROLE_TRAINER')")
    public ResponseEntity<PokemonDto> getPokemon(@RequestParam() Long id) {
        Pokemon pokemon = pokemonRepository.findById(id).orElse(null);
        if (pokemon == null) {
            return null;
        }
        return ResponseEntity.ok(new PokemonDto(pokemon));
    }

    @GetMapping("/list")
    @PreAuthorize("hasAnyRole('ROLE_USER', 'ROLE_ADMIN', 'ROLE_TRAINER')")
    public List<PokemonListItem> getPokemonList(@RequestParam(defaultValue="0") int page) {
        return pokemonService.getPokemonList(page);
    }

    @PostMapping(consumes="application/json")
    @PreAuthorize("hasAnyRole('ROLE_ADMIN', 'ROLE_TRAINER')")
    public Boolean savePokemon(@RequestBody Pokemon pokemon) {
        try {
            pokemonRepository.save(pokemon);
            System.out.println("Pokemon saved: " + pokemon.getName());
            return true;
        } catch (Exception e) {
            System.out.println(e.getMessage());
            return false;
        }
    }
}
