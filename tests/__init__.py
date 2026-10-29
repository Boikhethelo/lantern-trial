import os
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

# Let tests import game code (from game.game import Game) and find "resources/...".
sys.path.insert(0, str(ROOT / "src") )
os.chdir(ROOT)