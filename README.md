# 💚 Lantern Trials

Welcome to **Lantern Trials**, a text-based adventure game challenge where you'll use your Python skills to guide a rookie Green Lantern through the ancient halls of **Oa**, home of the Green Lantern Corps, in search of the lost power of the **Central Power Battery**.

---

## 📖 GameState Overview

The Guardians of the Universe have sealed the Central Power Battery behind three trials of the **Emotional Spectrum**. Your Lantern's ring is nearly out of charge, and the only way to recharge it is to prove yourself worthy.

To win the game, players must:

- Explore the map of Oa
- Solve 3 Spectrum trials
- Collect:
  - 💚 **Lens of Will**
  - 💙 **Lens of Hope**
  - 🧡 **Lens of Resolve** *(the "fear mastered" trial)*
- Unlock the final room: **The Central Power Battery Chamber**

---

## 🗂️ Project Structure

```text
lantern_trial/

```

---

## 👥 Characters

Hal Jordan,Sector 2814,Fearless,Reckless
John Stewart,Sector 2814,Disciplined,Haunted by Past Failures
Jessica Cruz,Sector 2814,Resilient,Crippling Anxiety
Kilowog,Sector 674,Mentor and Tough,Short Temper
```

Your player must be created from one of these entries in `game.py`.

---

## 🧭 Provided Rooms

A sample `game_data.json` will be provided with seven Oa-themed rooms and their connections:

- **Guardian Citadel** (start)
- **Corps Armory**
- **Hall of Lanterns**
- **Will Forge** (💚 Trial)
- **Garden of Mogo** (💙 Trial)
- **Void of Fear** (🧡 Trial)
- **Central Power Battery Chamber** (final room)

Each room entry in the JSON defines its name, description, exits (direction to room), and items. The Central Power Battery Chamber should start **locked**.

---

## 🧠 Trial Design (Specs Only)

Each trial is triggered when the player tries to `take` the lens in that room. A trial function should decide whether the lens is granted, denied, or already owned. These are the specs for each.

### 💚 Will Forge: Test of Willpower

- The player is asked to hold their ring's charge against an escalating challenge (for example, a series of timed prompts or a "resist the pull" sequence of choices).
- Failing should not end the game; it should drain something (a turn, a charge, a hint) and let the player try again.
- Must use at least one piece of player state (charge, inventory, or character trait).

### 💙 Garden of Mogo: Test of Hope

- The player is shown a sacrifice choice, such as giving up an inventory item to help a dying planet-garden bloom.
- The "right" answer should not be obvious from the item's name alone. Reward players who read the room description.
- The lens is only granted if the player actually parts with an item.

### 🧡 Void of Fear: Test of Courage

- The player must walk through a darkened sequence of rooms or prompts while their ring flickers.
- Include at least one choice that tempts the player to retreat.
- Success requires pushing forward through a minimum number of steps without using `go` to leave.


---

## 🎮 Player Commands Guide

| Command | Description |
|---|---|
| `move [direction]` | Move the player in a direction. E.g. `go north` |
| `look` | Show the current room's description, exits and visible items |
| `take [item]` | Pick up an item and add it to inventory (may trigger a trial) |
| `use [item]` | Use an inventory item. E.g. `use ring` could recharge or light a path |
| `inventory` | Show all items currently carried |
| `charge` | Show the ring's current charge level |
| `help` | List all commands with short descriptions |
| `save_game.py` | Save the current game state to a file |
| `load_game.py` | Load the previously saved game state |
| `quit` / `exit` | Exit the game loop |

### 🧑‍💻 Example Input/Output (format only)

```text
> look
You are in the Corps Armory.
Racks of dormant lantern batteries line the walls.
You see: spare battery, Guardian scroll
Exits: south, east

> take spare battery
You added the spare battery to your inventory.

> inventory
You are carrying: spare battery
```


---

## ⚔️ Challenges

Tackle these once the basics work. They're ordered roughly by difficulty.

1. **Ring Charge System:** The ring starts with limited charge. Moves and failed trials drain it, and reaching 0 means game over unless the player finds a way to recharge.
2. **Character-Driven Outcomes:** A Lantern's strength should make one trial easier (a hint, an extra attempt), and their weakness should make another harder.
3. **Locked Final Room:** The Battery Chamber must refuse entry until all three lenses are in inventory, with a different message depending on which are missing.
4. **Robust Save/Load:** Loading a save made mid-trial or with a missing file must not crash the game.
5. **Input Hardening:** Handle empty input, unknown commands, bad directions, and extra whitespace gracefully.
6. **No Hardcoding:** Rooms, items and exits must come from `game_data.json`, so editing the file changes the world without touching code.

---

## Extras

- Write tests for all your classes
- Store trial prompts in a JSON file and pick randomly
- Give each character a special power (e.g. Kilowog can brute-force a locked door once)
- Add a Sinestro-style rival who appears in rooms and drains charge
- Add a constructs system: `use ring` to create a temporary item (a bridge, a shield)
- Add colour using `colorama` (green for success, yellow for fear, blue for hope)

**Note:** Only attempt these once all basic functionality is in place.

---

## ✅ End Goal

Once the player has all 3 lenses and enters the **Central Power Battery Chamber**, display this:

> "The Spectrum has judged you. With will, hope, and courage, your ring burns brighter than ever. What will you do with such power?"

---

## 🧰 Evaluation Checklist

- [ ] GameState starts, runs, and exits cleanly
- [ ] All commands in the guide work
- [ ] 5+ characters load 
- [ ] All three trials are playable, winnable, and retryable
- [ ] Final room is locked until all lenses are collected
- [ ] Save/load restores the full game state
- [ ] Code is split sensibly across the provided files
- [ ] Tests exist for core classes (bonus)

---


