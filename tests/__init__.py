import os
from pathlib import Path

# The game reads files like "resources/game_data.json", so tests must run from src.
# This makes that true no matter where the tests are started from.
os.chdir(Path(__file__).resolve().parents[1])
