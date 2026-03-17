package edu.gatech.battle.battle;

import edu.gatech.battle.pokemon.PokemonSummaryDto;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.security.access.prepost.PreAuthorize;
import org.springframework.validation.annotation.Validated;
import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import java.util.List;

@Validated
@RestController
@RequestMapping("/battle")
@CrossOrigin(origins = "http://localhost:3001")
public class BattleController {

    @Autowired
    private BattleService battleService;

    @PostMapping(consumes="application/json")
     @PreAuthorize("hasAnyRole('ROLE_USER', 'ROLE_ADMIN', 'ROLE_TRAINER')")
    public Long initBattle(@RequestBody BattleRequest request) {
        return battleService.init(request).getId();
    }

    @GetMapping(value="/{id}")
    @PreAuthorize("hasAnyRole('ROLE_USER', 'ROLE_ADMIN', 'ROLE_TRAINER')")
    public BattleDto getBattle(@PathVariable Long id) {
        return battleService.getBattle(id);
    }

    @GetMapping(value="/pokemon")
    @PreAuthorize("hasAnyRole('ROLE_USER', 'ROLE_ADMIN', 'ROLE_TRAINER')")
    public List<PokemonSummaryDto> getPokemonList() { return battleService.getPokemonThatCanBattle(); }
}
