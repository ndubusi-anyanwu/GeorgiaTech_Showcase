package edu.gatech.battle.item;

import jakarta.transaction.Transactional;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.data.domain.PageRequest;
import org.springframework.data.domain.Pageable;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
public class ItemService {

    @Autowired
    private ItemRepository itemRepository;

    public List<Item> getAllItems(int page) {
        Pageable pageable = PageRequest.of(page, 48);
        return itemRepository.findAll(pageable).stream().toList();
    }

    private void saveItem(String name, String type, String effect, int value, boolean reusable) {
        if (!itemRepository.existsByName(name)) {
            Item item = new Item(name, type, effect, value, reusable);
            itemRepository.save(item);
        }
    }

    @Transactional
    public void initItemData() {
        // Initialize items and save
        saveItem("Oran Berry", "berry", "Restores 10 HP", 10, false);
        saveItem("Sitrus Berry", "berry", "Restores 30 HP", 30, false);
        saveItem("Potion", "potion", "Restores 20 HP", 20, false);
        saveItem("Leftovers", "holdable", "Restores HP gradually", 5, true);
    }
}
