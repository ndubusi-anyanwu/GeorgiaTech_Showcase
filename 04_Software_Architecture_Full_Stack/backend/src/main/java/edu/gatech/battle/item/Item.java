package edu.gatech.battle.item;

import jakarta.persistence.*;
import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;

@Entity
@Data
@NoArgsConstructor
@AllArgsConstructor
@Table(name = "items")
public class Item {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    @Column(nullable = false, unique = true)
    private String name;

    private String type;
    private String effect;
    private Integer value;
    private Boolean reusable;

    public Item(String name, String type, String effect, Integer value, Boolean reusable) {
        this.name = name;
        this.type = type;
        this.effect = effect;
        this.value = value;
        this.reusable = reusable;
    }
    public Boolean isReusable() {
        return reusable;
    }
}
