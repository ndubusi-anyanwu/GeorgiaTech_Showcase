CS 6310 Group 036 - Architectural Decision Record

Title: Configurability - Battle Configuration

Status: Proposed

Context: Add User configurability to each Pokemon battle so that there can be different play styles and reduced redundancy while battling Pokemon. Adding configurability to this application would provide more replayability. 

Decision: The configuration options for each Pokemon battle would be a turn limit, Pokemon aggressiveness, and battlefield background. The default turn limit would be unlimited (until a Pokemon faints), but this could be changed to a few different values to end after a set amount of turns. The aggressiveness for each Pokemon would affect the randomness move selection triggers, with the default being what is specified in the assignment. There would be two additional values, one for a more aggressive attacking approach and one for a more defensive approach. Lastly, there would be different battlefield backgrounds to chose from for display during the battle. 

Consequences: The advantages of this configuration is User flexibility for each battle. However this approach would add complexity and performance overhead, specifically for saving the various battleground images. 
