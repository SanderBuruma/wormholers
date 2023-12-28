# Game description
## Inspiration
The game takes inspiration from Eve Online's wormhole system, with known-space and wormhole-space. 

The game also takes inspiration from Eve Online's economy system and cosmic signature scanning & anomaly system.

The turn based resolution of games like Diplomacy is also taken as inspiration. Actions are planned during a turn and executed between turns.

Some inspiration is also taken from Ferion (now inactivate) in that matches are played out over days or weeks, whereas turns end on a timer.

The setting of the game is meant to be Utopian and pacifistic. This means that players are defined by lore to be friendly to each other and cooperative and that there are no hostile threats. Players cannot die in known-space. However, space itself can still be hostile (ie. lethal accidents can happen)

## Gameplay
The player starts out in k-space in a ship, with a complete map of where each known-space system leads and how.

There is no direct-currency such as USD or Credits. Barter will be the closest approximation.

Communication can only be done in-system. In wormhole-space ships are not visible by default, but must be scanned down before communication can be initiated.

The player can detect various signatures, which can be explored for various benefits. Signatures can be many things until identified, whether ruin, space station, asteroid, comet, ship or wormhole.

Ships cannot be easily identified as npc or player controlled. There will be many npc-actors throughout the game.

Players can die, and will have to restart from scratch if they do. Being in wormhole-space will deplete fuel. Once fuel runs out, ships go abandoned and the occupant dies permanently.

The player can have multiple ships they're in communication with. Ships in w-space cannot be controlled without lines of communication through relays at wormholes. If communication is lost they become inactivate and people may die after energy runs out. If a non-player pilot is lost in wormhole space, they may invent their own directives. Expiring wormhole connections are the biggest communication obstacle that players will have to deal with.

The player can assign lists of orders which npc-pilots can execute in succession even while out of communication. The whereabouts and status of out-of-communication ships will always be unknown to their owner.

## The Goal 
Each player's win condition is hidden, assigned at quasi-random (the player is given a few random options at the start). Goals can be anything from rescuing lost ships in w-space, to building a big ship, to finding a specific wormhole system, or building a station in w-space, etc

## Replays
All actions are recorded and are saved along with the map seed so that games can be replayed from scratch. NPC actions can be inferred from the recorded seed and player actions.

# Installation
- `pip install Django pyyaml`