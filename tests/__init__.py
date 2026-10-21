import os
import sys
from pathlib import Path

SRC = Path(__file__).resolve().parents[1] / "src"

# Let tests import game code (from game.game import Game) and find "resources/...".
sys.path.insert(0, str(SRC))
os.chdir(SRC)