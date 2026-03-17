package edu.gatech.battle.pokemon;

import com.fasterxml.jackson.databind.JsonNode;
import com.fasterxml.jackson.databind.ObjectMapper;
import edu.gatech.battle.model.Attack;
import edu.gatech.battle.model.Defense;
import edu.gatech.battle.item.Item;
import edu.gatech.battle.model.Type;
import edu.gatech.battle.item.ItemRepository;
import jakarta.transaction.Transactional;
import java.util.List;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.data.domain.PageRequest;
import org.springframework.data.domain.Pageable;
import org.springframework.data.domain.Sort;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.stereotype.Service;
import org.springframework.web.client.RestTemplate;

@Service
public class PokemonService {

    private final String pokeApiUrl = "https://pokeapi.co/api/v2/";

    @Autowired
    private PokemonRepository pokemonRepository;

    public List<PokemonListItem> getPokemonList(int page) {
        Pageable pageable = PageRequest.of(page, 48, Sort.by("name"));
        return pokemonRepository.findAll(pageable).stream().map(PokemonListItem::new).toList();
    }

    public Pokemon findById(Long id) {
        return pokemonRepository.findById(id).orElse(null);
    }

    public String getSprite(String name) {
        try {
            ResponseEntity<String> response = new RestTemplate().getForEntity(pokeApiUrl + "pokemon/" + name.toLowerCase() + "/", String.class);
            if (response.getStatusCode() != HttpStatus.OK) {
                return "";
            }
            JsonNode root = new ObjectMapper().readTree(response.getBody());
            return root.at("/sprites/front_default").textValue();
        } catch (Exception e) {
            return "";
        }
    }

    @Transactional
    public void initPokemonData() {
        // *********************************************************************
        // Create Attacks
        // *********************************************************************

        // Attack
        Attack attackSkill = new Attack();
        attackSkill.setName("Attack");
        attackSkill.setDamage(1);

        // Charm
        Attack charm = new Attack();
        charm.setName("Charm");
        charm.setDamage(0);

        // Confusion
        Attack confusion = new Attack();
        confusion.setName("Confusion");
        confusion.setDamage(3);

        // Curse
        Attack curse = new Attack();
        curse.setName("Curse");
        curse.setDamage(2);

        // Double Slap
        Attack doubleSlap = new Attack();
        doubleSlap.setName("Double Slap");
        doubleSlap.setDamage(10);

        // Earth Quake
        Attack earthQuake = new Attack();
        earthQuake.setName("Earth Quake");
        earthQuake.setDamage(3);

        // Ember
        Attack ember = new Attack();
        ember.setName("Ember");
        ember.setDamage(3);

        // Flamethrower
        Attack flamethrower = new Attack();
        flamethrower.setName("Flamethrower");
        flamethrower.setDamage(6);

        // Growl
        Attack growl = new Attack();
        growl.setName("Growl");
        growl.setDamage(1);

        // Gust
        Attack gust = new Attack();
        gust.setName("Gust");
        gust.setDamage(1);

        // Hydro Pump
        Attack hydroPump = new Attack();
        hydroPump.setName("Hydro Pump");
        hydroPump.setDamage(6);

        // Ice Beam
        Attack iceBeam = new Attack();
        iceBeam.setName("Ice Beam");
        iceBeam.setDamage(3);

        // Ice Shard
        Attack iceShard = new Attack();
        iceShard.setName("Ice Shard");
        iceShard.setDamage(2);

        // Imprison
        Attack imprison = new Attack();
        imprison.setName("Imprison");
        imprison.setDamage(2);

        // Leaf Storm
        Attack leafStorm = new Attack();
        leafStorm.setName("Leaf Storm");
        leafStorm.setDamage(6);

        // Mega Kick
        Attack megaKick = new Attack();
        megaKick.setName("Mega Kick");
        megaKick.setDamage(2);

        // Mega Punch
        Attack megaPunch = new Attack();
        megaPunch.setName("Mega Punch");
        megaPunch.setDamage(1);

        // Mist
        Attack mist = new Attack();
        mist.setName("Mist");
        mist.setDamage(1);

        // Poison
        Attack poison = new Attack();
        poison.setName("Poison");
        poison.setDamage(0);

        // Pound damage 1
        Attack pound_dmg1 = new Attack();
        pound_dmg1.setName("Pound");
        pound_dmg1.setDamage(1);

        // Pound damage 2
        Attack pound_dmg2 = new Attack();
        pound_dmg2.setName("Pound");
        pound_dmg2.setDamage(2);

        // Psychic damage 6
        Attack psychic_dmg6 = new Attack();
        psychic_dmg6.setName("Psychic");
        psychic_dmg6.setDamage(6);

        // Psychic damage 15
        Attack psychic_dmg15 = new Attack();
        psychic_dmg15.setName("Psychic");
        psychic_dmg15.setDamage(15);

        // Razor Leaf
        Attack razorLeaf = new Attack();
        razorLeaf.setName("Razor Leaf");
        razorLeaf.setDamage(3);

        // Rest
        Attack rest = new Attack();
        rest.setName("Rest");
        rest.setDamage(0);

        // Rock Slide
        Attack rockSlide = new Attack();
        rockSlide.setName("Rock Slide");
        rockSlide.setDamage(6);

        // Rock Throw
        Attack rockThrow = new Attack();
        rockThrow.setName("Rock Throw");
        rockThrow.setDamage(2);

        // Scratch
        Attack scratch = new Attack();
        scratch.setName("Scratch");
        scratch.setDamage(2);

        // Seismic Toss
        Attack seismicToss = new Attack();
        seismicToss.setName("Seismic Toss");
        seismicToss.setDamage(3);

        // Sharpie
        Attack sharpie = new Attack();
        sharpie.setName("Sharpie");
        sharpie.setDamage(0);

        // Sheer Cold
        Attack sheerCold = new Attack();
        sheerCold.setName("Sheer Cold");
        sheerCold.setDamage(6);

        // Sing
        Attack sing = new Attack();
        sing.setName("Sing");
        sing.setDamage(1);

        // Snore
        Attack snore = new Attack();
        snore.setName("Snore");
        snore.setDamage(6);

        // Solar Beam
        Attack solarBeam = new Attack();
        solarBeam.setName("Solar Beam");
        solarBeam.setDamage(6);

        // Tackle damage 1
        Attack tackle_dmg1 = new Attack();
        tackle_dmg1.setName("Tackle");
        tackle_dmg1.setDamage(1);

        // Tackle damage 2
        Attack tackle_dmg2 = new Attack();
        tackle_dmg2.setName("Tackle");
        tackle_dmg2.setDamage(2);

        // Tail Whip
        Attack tailWhip = new Attack();
        tailWhip.setName("Tail Whip");
        tailWhip.setDamage(2);

        // Thunder
        Attack thunder = new Attack();
        thunder.setName("Thunder");
        thunder.setDamage(6);

        // Thunder Shock
        Attack thunderShock = new Attack();
        thunderShock.setName("Thunder Shock");
        thunderShock.setDamage(3);

        // Transform
        Attack transform = new Attack();
        transform.setName("Transform");
        transform.setDamage(0);

        // Vine Whip
        Attack vineWhip = new Attack();
        vineWhip.setName("Vine Whip");
        vineWhip.setDamage(2);

        // Water Gun
        Attack waterGun = new Attack();
        waterGun.setName("Water Gun");
        waterGun.setDamage(3);

        // Whirlwind
        Attack whirlwind = new Attack();
        whirlwind.setName("Whirlwind");
        whirlwind.setDamage(2);

        // *********************************************************************
        // Create Defenses
        // *********************************************************************

        // Block
        Defense block = new Defense();
        block.setName("Block");
        block.setDamageReduction(2);

        // Endure
        Defense endure = new Defense();
        endure.setName("Endure");
        endure.setDamageReduction(1);

        // Heal Pulse
        Defense healPulse = new Defense();
        healPulse.setName("Heal Pulse");
        healPulse.setDamageReduction(0);

        // Protect
        Defense protect = new Defense();
        protect.setName("Protect");
        protect.setDamageReduction(3);

        // *********************************************************************
        // Create Pokemon
        // *********************************************************************

        // Pikachu
        Pokemon pikachu = new Pokemon();
        pikachu.setName("Pikachu");
        pikachu.setHp(25);
        pikachu.setAttackSkills(List.of(growl, tailWhip, thunderShock, thunder));
        pikachu.setDefenseSkills(List.of(endure, block, protect));
        pikachu.setTypes(List.of(Type.Electric));
        pikachu.setWeaknesses(List.of(Type.Ground));
        pikachu.setAttack(55);
        pikachu.setDefense(40);
        pikachu.setSpecialAttack(50);
        pikachu.setSpecialDefense(50);
        pikachu.setSpeed(90);
        pikachu.setCritRate(4);
        pikachu.setHeight(0.4F);
        pikachu.setWeight(6.0F);
        pikachu.setCategory("Mouse");
        pikachu.setAbilities("Static");
        pikachu.setGender(1);
        pokemonRepository.save(pikachu);

        // Abra
        Pokemon abra = new Pokemon();
        abra.setName("Abra");
        abra.setHp(25);
        abra.setAttackSkills(List.of(megaPunch, megaKick, seismicToss, psychic_dmg6));
        abra.setDefenseSkills(List.of(endure, block, protect));
        abra.setTypes(List.of(Type.Psychic));
        abra.setWeaknesses(List.of(Type.Bug, Type.Ghost, Type.Dark));
        abra.setAttack(20);
        abra.setDefense(15);
        abra.setSpecialAttack(105);
        abra.setSpecialDefense(55);
        abra.setSpeed(90);
        abra.setCritRate(4);
        abra.setHeight(0.9F);
        abra.setWeight(19.5F);
        abra.setCategory("Psi");
        abra.setAbilities("Inner Focus");
        abra.setGender(0);
        pokemonRepository.save(abra);

        // Bulbasaur
        Pokemon bulbasaur = new Pokemon();
        bulbasaur.setName("Bulbasaur");
        bulbasaur.setHp(25);
        bulbasaur.setAttackSkills(List.of(tackle_dmg1, vineWhip, razorLeaf, leafStorm));
        bulbasaur.setDefenseSkills(List.of(endure, block, protect));
        bulbasaur.setTypes(List.of(Type.Grass, Type.Poison));
        bulbasaur.setWeaknesses(List.of(Type.Fire, Type.Ice, Type.Flying, Type.Psychic));
        bulbasaur.setAttack(49);
        bulbasaur.setDefense(49);
        bulbasaur.setSpecialAttack(65);
        bulbasaur.setSpecialDefense(65);
        bulbasaur.setSpeed(45);
        bulbasaur.setCritRate(4);
        bulbasaur.setHeight(0.7F);
        bulbasaur.setWeight(6.9F);
        bulbasaur.setCategory("Seed");
        bulbasaur.setAbilities("Overgrow");
        bulbasaur.setGender(0);
        pokemonRepository.save(bulbasaur);

        // Butterfree
        Pokemon butterfree = new Pokemon();
        butterfree.setName("Butterfree");
        butterfree.setHp(40);
        butterfree.setAttackSkills(List.of(poison, gust, whirlwind, solarBeam));
        butterfree.setDefenseSkills(List.of(endure, block, protect));
        butterfree.setTypes(List.of(Type.Bug, Type.Flying));
        butterfree.setWeaknesses(List.of(Type.Fire, Type.Electric, Type.Ice, Type.Flying, Type.Rock));
        butterfree.setAttack(45);
        butterfree.setDefense(50);
        butterfree.setSpecialAttack(90);
        butterfree.setSpecialDefense(80);
        butterfree.setSpeed(70);
        butterfree.setCritRate(4);
        butterfree.setHeight(1.1F);
        butterfree.setWeight(32.0F);
        butterfree.setCategory("Butterfly");
        butterfree.setAbilities("Compound Eyes");
        butterfree.setGender(1);
        pokemonRepository.save(butterfree);

        // Charmander
        Pokemon charmander = new Pokemon();
        charmander.setName("Charmander");
        charmander.setHp(25);
        charmander.setAttackSkills(List.of(attackSkill, scratch, ember, flamethrower));
        charmander.setDefenseSkills(List.of(endure, block, protect));
        charmander.setTypes(List.of(Type.Fire));
        charmander.setWeaknesses(List.of(Type.Water, Type.Ground, Type.Rock));
        charmander.setAttack(52);
        charmander.setDefense(43);
        charmander.setSpecialAttack(60);
        charmander.setSpecialDefense(50);
        charmander.setSpeed(65);
        charmander.setCritRate(4);
        charmander.setHeight(0.6F);
        charmander.setWeight(8.5F);
        charmander.setCategory("Lizard");
        charmander.setAbilities("Blaze");
        charmander.setGender(0);
        pokemonRepository.save(charmander);

        // Ditto
        Pokemon ditto = new Pokemon();
        ditto.setName("Ditto");
        ditto.setHp(35);
        ditto.setAttackSkills(List.of(transform));
        ditto.setDefenseSkills(List.of(endure, block, protect));
        ditto.setTypes(List.of(Type.Normal));
        ditto.setWeaknesses(List.of(Type.Fighting));
        ditto.setAttack(48);
        ditto.setDefense(48);
        ditto.setSpecialAttack(48);
        ditto.setSpecialDefense(48);
        ditto.setSpeed(48);
        ditto.setCritRate(4);
        ditto.setHeight(0.3F);
        ditto.setWeight(4.0F);
        ditto.setCategory("Transform");
        ditto.setAbilities("Limber");
        ditto.setGender(0);
        pokemonRepository.save(ditto);

        // Ekans
        Pokemon ekans = new Pokemon();
        ekans.setName("Ekans");
        ekans.setHp(35);
        ekans.setAttackSkills(List.of(poison, tailWhip));
        ekans.setDefenseSkills(List.of(endure, block, protect));
        ekans.setTypes(List.of(Type.Poison));
        ekans.setWeaknesses(List.of(Type.Ground, Type.Psychic));
        ekans.setAttack(60);
        ekans.setDefense(44);
        ekans.setSpecialAttack(40);
        ekans.setSpecialDefense(54);
        ekans.setSpeed(55);
        ekans.setCritRate(4);
        ekans.setHeight(2.0F);
        ekans.setWeight(6.9F);
        ekans.setCategory("Snake");
        ekans.setAbilities("Shed Skin");
        ekans.setGender(1);
        pokemonRepository.save(ekans);

        // Geodude
        Pokemon geodude = new Pokemon();
        geodude.setName("Geodude");
        geodude.setHp(25);
        geodude.setAttackSkills(List.of(tackle_dmg1, rockThrow, earthQuake, rockSlide));
        geodude.setDefenseSkills(List.of(endure, block, protect));
        geodude.setTypes(List.of(Type.Rock, Type.Ground));
        geodude.setWeaknesses(List.of(Type.Water, Type.Grass, Type.Ice, Type.Fighting, Type.Ground, Type.Steel));
        geodude.setAttack(80);
        geodude.setDefense(100);
        geodude.setSpecialAttack(30);
        geodude.setSpecialDefense(30);
        geodude.setSpeed(20);
        geodude.setCritRate(4);
        geodude.setHeight(0.4F);
        geodude.setWeight(20.0F);
        geodude.setCategory("Rock");
        geodude.setAbilities("Rock Head");
        geodude.setGender(0);
        pokemonRepository.save(geodude);

        // Jigglypuff
        Pokemon jigglypuff = new Pokemon();
        jigglypuff.setName("Jigglypuff");
        jigglypuff.setHp(25);
        jigglypuff.setAttackSkills(List.of(sharpie, sing, pound_dmg2, doubleSlap));
        jigglypuff.setDefenseSkills(List.of(endure, block, protect));
        jigglypuff.setTypes(List.of(Type.Normal, Type.Fairy));
        jigglypuff.setWeaknesses(List.of(Type.Poison, Type.Steel));
        jigglypuff.setAttack(45);
        jigglypuff.setDefense(20);
        jigglypuff.setSpecialAttack(45);
        jigglypuff.setSpecialDefense(25);
        jigglypuff.setSpeed(20);
        jigglypuff.setCritRate(4);
        jigglypuff.setHeight(0.5F);
        jigglypuff.setWeight(5.5F);
        jigglypuff.setCategory("Balloon");
        jigglypuff.setAbilities("Cute Charm");
        jigglypuff.setGender(1);
        pokemonRepository.save(jigglypuff);

        // Lapras
        Pokemon lapras = new Pokemon();
        lapras.setName("Lapras");
        lapras.setHp(25);
        lapras.setAttackSkills(List.of(mist, iceShard, iceBeam, sheerCold));
        lapras.setDefenseSkills(List.of(endure, block, protect));
        lapras.setTypes(List.of(Type.Water, Type.Ice));
        lapras.setWeaknesses(List.of(Type.Electric, Type.Grass, Type.Rock, Type.Fighting));
        lapras.setAttack(85);
        lapras.setDefense(80);
        lapras.setSpecialAttack(85);
        lapras.setSpecialDefense(95);
        lapras.setSpeed(60);
        lapras.setCritRate(4);
        lapras.setHeight(2.5F);
        lapras.setWeight(220.0F);
        lapras.setCategory("Transport");
        lapras.setAbilities("Water Absorb");
        lapras.setGender(1);
        pokemonRepository.save(lapras);

        // Mew
        Pokemon mew = new Pokemon();
        mew.setName("Mew");
        mew.setHp(25);
        mew.setAttackSkills(List.of(charm, pound_dmg1, imprison, psychic_dmg15));
        mew.setDefenseSkills(List.of(endure, block, protect));
        mew.setTypes(List.of(Type.Psychic));
        mew.setWeaknesses(List.of(Type.Bug, Type.Ghost, Type.Dark));
        mew.setAttack(100);
        mew.setDefense(100);
        mew.setSpecialAttack(100);
        mew.setSpecialDefense(100);
        mew.setSpeed(100);
        mew.setCritRate(4);
        mew.setHeight(0.4F);
        mew.setWeight(4.0F);
        mew.setCategory("New Species");
        mew.setAbilities("Synchronize");
        mew.setGender(1);
        pokemonRepository.save(mew);

        // Rattata
        Pokemon rattata = new Pokemon();
        rattata.setName("Rattata");
        rattata.setHp(25);
        rattata.setAttackSkills(List.of(scratch, tackle_dmg1));
        rattata.setDefenseSkills(List.of(endure, block, protect));
        rattata.setTypes(List.of(Type.Normal));
        rattata.setWeaknesses(List.of(Type.Fighting));
        rattata.setAttack(56);
        rattata.setDefense(35);
        rattata.setSpecialAttack(25);
        rattata.setSpecialDefense(35);
        rattata.setSpeed(72);
        rattata.setCritRate(4);
        rattata.setHeight(0.3F);
        rattata.setWeight(3.5F);
        rattata.setCategory("Mouse");
        rattata.setAbilities("Run Away");
        rattata.setGender(0);
        pokemonRepository.save(rattata);

        // Slowpoke
        Pokemon slowpoke = new Pokemon();
        slowpoke.setName("Slowpoke");
        slowpoke.setHp(25);
        slowpoke.setAttackSkills(List.of(tackle_dmg1, curse, confusion, psychic_dmg6));
        slowpoke.setDefenseSkills(List.of(healPulse, endure, block, protect));
        slowpoke.setTypes(List.of(Type.Water, Type.Psychic));
        slowpoke.setWeaknesses(List.of(Type.Grass, Type.Electric, Type.Bug, Type.Ghost, Type.Dark));
        slowpoke.setAttack(65);
        slowpoke.setDefense(65);
        slowpoke.setSpecialAttack(40);
        slowpoke.setSpecialDefense(40);
        slowpoke.setSpeed(15);
        slowpoke.setCritRate(4);
        slowpoke.setHeight(1.2F);
        slowpoke.setWeight(36.0F);
        slowpoke.setCategory("Dopey");
        slowpoke.setAbilities("Oblivious");
        slowpoke.setGender(0);
        pokemonRepository.save(slowpoke);

        // Snorlax
        Pokemon snorlax = new Pokemon();
        snorlax.setName("Snorlax");
        snorlax.setHp(40);
        snorlax.setAttackSkills(List.of(rest, snore));
        snorlax.setDefenseSkills(List.of(healPulse, endure, block, protect));
        snorlax.setTypes(List.of(Type.Normal));
        snorlax.setWeaknesses(List.of(Type.Fighting));
        snorlax.setAttack(110);
        snorlax.setDefense(65);
        snorlax.setSpecialAttack(65);
        snorlax.setSpecialDefense(110);
        snorlax.setSpeed(30);
        snorlax.setCritRate(4);
        snorlax.setHeight(2.1F);
        snorlax.setWeight(460.0F);
        snorlax.setCategory("Sleeping");
        snorlax.setAbilities("Thick Fat");
        snorlax.setGender(0);
        pokemonRepository.save(snorlax);

        // Squirtle
        Pokemon squirtle = new Pokemon();
        squirtle.setName("Squirtle");
        squirtle.setHp(25);
        squirtle.setAttackSkills(List.of(attackSkill, tackle_dmg2, waterGun, hydroPump));
        squirtle.setDefenseSkills(List.of(healPulse, endure, block, protect));
        squirtle.setTypes(List.of(Type.Water));
        squirtle.setWeaknesses(List.of(Type.Grass, Type.Electric));
        squirtle.setAttack(48);
        squirtle.setDefense(65);
        squirtle.setSpecialAttack(50);
        squirtle.setSpecialDefense(64);
        squirtle.setSpeed(43);
        squirtle.setCritRate(4);
        squirtle.setHeight(0.5F);
        squirtle.setWeight(9.0F);
        squirtle.setCategory("Tiny Turtle");
        squirtle.setAbilities("Torrent");
        squirtle.setGender(0);
        pokemonRepository.save(squirtle);

        // Vulpix
        Pokemon vulpix = new Pokemon();
        vulpix.setName("Vulpix");
        vulpix.setHp(38);
        vulpix.setAttackSkills(List.of(tackle_dmg1, tailWhip));
        vulpix.setDefenseSkills(List.of(healPulse, endure, block, protect));
        vulpix.setTypes(List.of(Type.Fire));
        vulpix.setWeaknesses(List.of(Type.Ground, Type.Water, Type.Rock));
        vulpix.setAttack(41);
        vulpix.setDefense(40);
        vulpix.setSpecialAttack(50);
        vulpix.setSpecialDefense(65);
        vulpix.setSpeed(65);
        vulpix.setCritRate(4);
        vulpix.setHeight(0.6F);
        vulpix.setWeight(9.9F);
        vulpix.setCategory("Fox");
        vulpix.setAbilities("Flash Fire");
        vulpix.setGender(0);
        pokemonRepository.save(vulpix);
    }
}
