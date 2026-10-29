# 💚 Lantern Trials

A text-based adventure game set in the world of the Green Lantern Corps, written in Python.

The Central Power Battery on Oa has developed a fault. It no longer connects Lanterns to the emotional spectrum, and your ring is down to **one last charge**. Explore the Corps' halls, pass three trials to collect three lenses, then enter the Central Power Battery Chamber, complete the final trial, and speak the oath to recharge your ring.

> *Green Lantern and related characters are trademarks of DC Comics. This is a fan-made learning project and is not affiliated with DC.*

---

## 📖 The Goal

**To win:**

1. Explore the map of Oa.
2. Pass the three lens trials and collect:
   - 💚 **Lens of Will** (Will Forge)
   - 💙 **Lens of Hope** (Garden of Mogo)
   - 🧡 **Lens of Resolve** (Void of Fear)
3. Enter the **Central Power Battery Chamber** (it unlocks once you hold all three lenses).
4. Complete the final trial and say the oath to recharge your ring.

**To lose:** your ring's charge reaches 0.

---

## 🚀 Quick Start

**Requirements:** Python 3.10 or newer.

```bash
git clone https://github.com/Boikhethelo/lantern-trial.git
cd lantern-trial
pip install -r requirements.txt
python src/play.py
```

Run the game **from the project root** (the folder that contains `src/`, `resources/` and `tests/`), because the game loads its data from `resources/`.

At the start you can type `load` to continue a saved game, or press Enter to begin a new one. You then pick a character and a difficulty from 1 (easy) to 3 (hard).

---

## 🎮 Commands

| Command | What it does |
|---|---|
| `go [direction]` | Move `north`, `south`, `east` or `west`. Locked rooms refuse you. |
| `look` | Show the room, the items you can see, and the exits. |
| `take [item]` | Pick up an item. Lenses start a trial first. |
| `use [item]` | Use an item. In the Chamber, the lenses are used for the final trial. |
| `inventory` | List what you are carrying. |
| `charge` | Show your ring's remaining charge. |
| `help` | List the available commands. |
| `save` | Save your game. |
| `load` | Load your saved game. |
| `quit` / `exit` | Leave the game. |

During a trial you can also type `hint` for a hint (if your Lantern has one) or `leave` to walk away.

### Example

```text
What would you like to do next : look
You are in Guardian Citadel. The ancient seat of the Guardians, humming with green light.
You see: nothing
Exits: east

What would you like to do next : take lens of hope
Mogo is a Green Lantern, but he is also a living what?
what is your answer? hint
He is enormous and round, and you are standing on him.
what is your answer? planet
Correct! lens of hope has been added to your inventory
Will Forge has been unlocked
```

---

## ⚡ Charge

Your ring starts with **100 charge**, and everything you do spends it:

| Action | Cost |
|---|---|
| Any valid command | 1 |
| `take` (on top of the command) | 10 |
| Starting a lens trial | 10 |
| `use` (on top of the command) | 5 |

So each lens costs about 21 charge, and wasted commands add up. Typos and `quit` are free. When your charge reaches 0, the game is over.

---

## 🧭 The World

```text
                         [Will Forge] 🔒
                               |
[Guardian Citadel]--[Corps Armory]--[Hall of Lanterns]--[Void of Fear]--[Central Power Battery Chamber] 🔒
                                          |
                                   [Garden of Mogo]

🔒 = starts locked
```

| Room | Contents | Notes |
|---|---|---|
| Guardian Citadel | nothing | Start here. |
| Corps Armory | spare battery, Guardian scroll | Ordinary items. |
| Hall of Lanterns | lantern oath tablet | The hub, with four exits. |
| Garden of Mogo | 💙 Lens of Hope | Trial of hope. |
| Will Forge | 💚 Lens of Will | Locked until you hold the Lens of Hope. Trial of willpower. |
| Void of Fear | 🧡 Lens of Resolve | Trial of courage. |
| Central Power Battery Chamber | final trial | Locked until you hold all three lenses. |

---

## 🧠 Trials

Taking a lens starts a trial. A question is drawn at random from the database for that room, at your chosen difficulty (or the nearest one if that room has none).

- **Answer** the question to collect the lens.
- **`hint`** shows a hint. Some hints are only given to one Lantern (for example, Kilowog gets a hint about Oa because he trained rookies there). Other Lanterns see "No hint for your Lantern on this one".
- **`leave`** walks away without the lens.
- If a room has no question available, the lens is gifted to you.

Questions are Green Lantern trivia and riddles, and every trial room has questions at all three difficulty levels.

---

## 👥 Characters

Pick one at the start. Characters come from `resources/characters.json`.

| Name | Sector | Strength | Weakness |
|---|---|---|---|
| Hal Jordan | 2814 | Fearless | Reckless |
| John Stewart | 2814 | Disciplined | Haunted by Past Failures |
| Jessica Cruz | 2814 | Resilient | Crippling Anxiety |
| Kilowog | 674 | Mentor and Tough | Short Temper |

---

## 💾 Saving and Loading

`save` writes `resources/save_file.json`, and `load` restores it (from the start menu or in game). A save stores:

- your character, charge and difficulty,
- your inventory and position,
- the state of every room (items left, locked or unlocked).

The save file is ignored by git. If it is missing or empty, `load` tells you there is no saved game.

---

## 🗂️ Project Structure

```text
lantern-trial/
├── README.md
├── requirements.txt          # rich (for the title and intro screens)
├── resources/
│   ├── game_data.json        # rooms, exits, items, locks and trial rules
│   ├── characters.json       # playable Lanterns
│   ├── questions.db          # SQLite database of trial questions
│   ├── schema.sql            # creates and seeds the questions table
│   └── save_file.json        # created by `save` (git-ignored)
├── src/
│   ├── play.py               # game loop and the composition root, build()
│   ├── menu/                 # start menu: new game or load
│   ├── router/               # maps command words to handlers
│   ├── handlers/             # move, take, save, load, use, unlock
│   ├── trial/                # runs a question trial
│   ├── rules/                # what can be entered and what unlocks
│   ├── game/                 # Game state and GameFactory
│   ├── room/ player/ question/   # data classes and their DAOs
│   ├── database/             # SQLite access for questions
│   ├── persistence/          # SaveStore: reads and writes plain dictionaries
│   ├── validation/           # input validation
│   └── display/              # all printing (uses rich)
└── tests/                    # unit tests, with helpers and fakes
```

### Data files

**`game_data.json`** describes the whole map. Each room looks like this:

```json
"Will Forge": {
  "description": "Molten green energy pours through channels in the floor.",
  "exits": { "south": "Hall of Lanterns" },
  "items": ["Lens of Will"],
  "locked": true,
  "requires": ["lens of hope"],
  "trial_items": ["lens of will"]
}
```

- `locked` is whether the room starts locked.
- `requires` lists the items that unlock it automatically.
- `trial_items` lists items that start a trial when taken.

**`questions` table** (in `questions.db`, rebuilt by `schema.sql`):

| Column | Meaning |
|---|---|
| `room` | Which trial room asks it |
| `difficulty` | 1 easy, 2 medium, 3 hard |
| `question` / `answer` | The question and its lowercase answer |
| `hint` | Optional hint |
| `character` | `NULL` means everyone sees the hint, otherwise only that Lantern |

---

## 🏗️ Design

The code is layered so that each class has one job and the pieces are handed to each other, not created inside each other:

- **Single responsibility:** `Game` holds state, `GameFactory` builds games, `Rules` decides what unlocks, `TrialController` runs a trial, `SaveStore` does file access, `Router` maps commands, and `Play` only runs the loop.
- **Open for extension:** new commands, rooms, requirements, characters and questions are added as data or one new entry, not by rewriting logic.
- **Dependency injection:** `build()` in `play.py` is the only place that creates the concrete classes. Everything else receives its collaborators, including the `ask` and `show` functions used for input and output, so the pieces can be tested with fakes.
- **Persistence knows nothing about the game:** `SaveStore` only reads and writes dictionaries, and `Game.snapshot()` produces one.

### Extending the game

- **New character:** add an entry to `resources/characters.json`.
- **New question:** insert a row into the `questions` table (or add it to `schema.sql`).
- **New room or lock:** add it to `game_data.json`, with `requires` and `trial_items` as needed.
- **New command:** add an entry to the dictionary in `src/router/router.py`, and add the word to the valid list in `src/validation/input_validator.py`.

---

## 🧪 Tests

The tests use Python's built-in `unittest`. Run them from the project root:

```bash
python -m unittest discover -s tests -t .
```

Run a single file with:

```bash
python -m unittest tests.test_rules -v
```

Most tests use small fakes from `tests/helpers.py` (for example a fake question source), so they need no database, no keyboard and no files.

---

