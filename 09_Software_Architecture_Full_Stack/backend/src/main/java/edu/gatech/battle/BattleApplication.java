package edu.gatech.battle;

import java.util.Random;
import java.util.List;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.security.access.prepost.PreAuthorize;
import org.springframework.web.bind.annotation.*;
import org.springframework.beans.factory.annotation.Autowired;

@SpringBootApplication
@RestController
@CrossOrigin(origins = "http://localhost:3001")
public class BattleApplication {

    // NOTE: autowired is a special annotation provided by the spring framework 
    // for enable dependency injection
    @Autowired
    private RandomNumberRepository repository;

	public static void main(String[] args) {
	    SpringApplication.run(BattleApplication.class, args);
	}

    @GetMapping("/random")
    @PreAuthorize("hasAnyRole('ROLE_USER', 'ROLE_ADMIN', 'ROLE_TRAINER')")
    public RandomNumber random() {
        Random rand = new Random();
        RandomNumber num = new RandomNumber(rand.nextInt());
        repository.save(num);
        return num;
    }

    @GetMapping("/list")
    @PreAuthorize("hasAnyRole('ROLE_USER', 'ROLE_ADMIN', 'ROLE_TRAINER')")
    public List<RandomNumber> list() {
        return repository.findAll();
    }
}
