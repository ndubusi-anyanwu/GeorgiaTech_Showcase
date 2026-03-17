CS 6310 Group 036 - Architectural Decision Record

Title: Pokemon Items

Status: Proposed

Context: Add variability and additional randomness to each Pokemon battle. Although the same Pokemon can battle repeatedly with different outcomes already, adding another variable of randomness by introducing various items would create more strategy than just picking the same 2 Pokemon to battle. 

Decision: There would be 5 different items in the game that could be used by the Pokemon. Each Pokemon has one spot for an item and an item has a single use during a battle. 

- Item to raise current HP to full upon use

- Item to double the damage of the next attack

- Item to double the defense of the next defend

- Item to cancel a defense of the other Pokemon

- Item to block an attack from the other Pokemon

The items are given to the Pokemon randomly or can be initialized prior to the battle. 

Consequences: The advantages of this configuration is battle variability for each battle. However this approach would add complexity and result in an additional class to the software architecture. 
