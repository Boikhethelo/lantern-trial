import os
import sys
import time

from rich import box
from rich.align import Align
from rich.console import Console
from rich.live import Live
from rich.panel import Panel
from rich.rule import Rule
from rich.table import Table
from rich.text import Text

console = Console()

# Set LANTERN_FAST=1 to skip every delay (handy while developing or testing).
FAST = os.environ.get("LANTERN_FAST") == "1"


# ---------- BUILDING BLOCKS ----------

def clear_screen():
    console.clear()


def pause(seconds=1.5):
    if not FAST:
        time.sleep(seconds)


def type_text(text, delay=0.035, style="white"):
    """Print text character by character for cinematic narration."""
    for char in text:
        console.print(char, end="", style=style, markup=False, highlight=False)
        sys.stdout.flush()
        if not FAST:
            time.sleep(delay)
    console.print()


def slow_print(text, delay=0.06, style="white"):
    type_text(text, delay, style)


def dramatic_pause(seconds=2):
    pause(seconds)


def scene(title, color):
    """Start a new scene: clear the screen and show its heading."""
    clear_screen()
    console.print(Rule(f"[bold {color}]{title}[/bold {color}]"))
    pause(0.5)


def line(text, delay=0.03, style="white", wait=1):
    """One narrated line, followed by a short beat."""
    type_text(text + "\n", delay, style)
    pause(wait)


def status_panel(text, title=None, color="red", box_style=box.HEAVY, padding=(1, 3)):
    """A centred block of text in a panel, like the ring's own display."""
    console.print()
    console.print(
        Panel(
            Align.center(Text(text, style=f"bold {color}", justify="center")),
            title=f"[bold {color}]{title}[/bold {color}]" if title else None,
            border_style=color,
            box=box_style,
            padding=padding,
        )
    )


# ---------- TITLE ----------

def show_title():
    clear_screen()

    title = r"""
 _        ___    _   _ _____ ___ ___ _  _
| |      / _ \  | \ | |_   _|   \_ _| \| |
| |__   | (_) | |  \| | | | | |) | || .` |
|____|   \___/  |_|\__| |_| |___/___|_|\_|

              T H E   L A N T E R N   T R I A L S
"""

    console.print(Align.center(Text(title, style="bold bright_green"), vertical="middle"))
    pause(1.5)

    console.print(
        Align.center(
            "[italic bright_white]When the universe goes dark, "
            "even the brightest must face the end.[/italic bright_white]"
        )
    )
    pause(2)


# ---------- THE STORY (about one minute) ----------

def opening_cinematic():
    show_title()

    # THE WAR OF LIGHT
    scene("THE WAR OF LIGHT", "red")
    line("For eons, the light endured.", 0.04, "bright_white")
    line("Then came the War of Light. Worlds burned. Corps fell.", 0.04, "red")
    line("And at last... the war ended.", 0.05, "bright_white", wait=1.5)

    status_panel(
        "VICTORY WAS WON.\nBUT THE LIGHT WAS NOT SAVED.",
        color="white", box_style=box.DOUBLE, padding=(1, 4),
    )
    pause(2)

    # THE SILENCE
    scene("THE SILENCE", "yellow")
    line("Deep within the Lantern Corps stood the Central Power Battery,", 0.03, "bright_yellow", wait=0.5)
    line("the beacon that connected every Lantern to the light.", 0.03, "white", wait=1)
    line("Then a fault tore through its core.", 0.04, "bold red", wait=1)
    line("Its light flickered... and began to die.", 0.05, "yellow", wait=1)

    status_panel(
        "POWER FLOW: DISRUPTED\nRING RECHARGING: OFFLINE\nCENTRAL BATTERY: CRITICAL",
        title="SYSTEM FAILURE",
    )
    pause(2)

    # THE ONLY HOPE
    scene("THE ONLY HOPE", "bright_green")
    line("Ancient records speak of three legendary lenses,", 0.03, "white", wait=0.5)
    line("three trials, and the way to restore the light.", 0.03, "bright_white", wait=1)

    lenses = [
        ("LENS OF HOPE", "To believe that light can return.", "bright_cyan"),
        ("LENS OF WILL", "To stand unbroken when everything says surrender.", "bright_green"),
        ("LENS OF RESOLVE", "To press on when the cost may be everything.", "bright_yellow"),
    ]
    for name, description, color in lenses:
        console.print()
        console.print(
            Panel(
                Align.center(
                    Text.from_markup(
                        f"[bold {color}]{name}[/bold {color}]\n"
                        f"[italic white]{description}[/italic white]",
                        justify="center",
                    )
                ),
                border_style=color,
                box=box.DOUBLE,
                padding=(0, 3),
            )
        )
        pause(1.2)
    pause(1)

    # YOUR FINAL CHARGE
    scene("YOUR FINAL CHARGE", "red")
    line("Your ring is all that stands between you and the darkness.", 0.03, "white", wait=0.5)
    line("Its light is fading. You have no second charge.", 0.04, "yellow", wait=0.5)
    line("Every step will consume power. Every trial will demand more.", 0.03, "yellow", wait=1)
    line("YOUR RING CANNOT RECHARGE.", 0.07, "bold red", wait=1)

    status_panel(
        "CHARGE REMAINING: CRITICAL\nRECHARGING: IMPOSSIBLE\nMISSION: RESTORE THE LIGHT",
        title="RING STATUS", color="bright_green",
    )
    pause(2)

    # THE TRIALS BEGIN
    clear_screen()
    line("The Corps does not need another hero who can win a war.", 0.03, "white", wait=1)
    line("It needs someone who can bring the light home.", 0.035, "bright_green", wait=1.5)

    console.print()
    console.print(Align.center(Text("THE LANTERN TRIALS BEGIN.", style="bold bright_green")))
    pause(1.5)

    console.print()
    console.input("[bold white]Press ENTER to begin your trials...[/bold white]")


# ---------- IN-GAME SCREENS ----------

def view_help():
    """The ring's command list."""
    commands = Table(box=box.SIMPLE_HEAVY, border_style="bright_green", header_style="bold bright_green")
    commands.add_column("COMMAND", style="bold white", no_wrap=True)
    commands.add_column("WHAT IT DOES", style="white")

    for command, description in [
        ("go [direction]", "Move north, south, east or west"),
        ("look", "Describe the room, its items and its exits"),
        ("take [item]", "Pick up an item (lenses start a trial)"),
        ("use [item]", "Use an item from your inventory"),
        ("inventory", "List what you are carrying"),
        ("charge", "Check your ring's remaining charge"),
        ("save / load", "Save or restore your game"),
        ("help", "Show this screen"),
        ("quit / exit", "Leave the game"),
    ]:
        commands.add_row(Text(command), description)   # Text, so [direction] is not read as markup

    trial = Table(box=box.SIMPLE_HEAVY, border_style="bright_yellow", header_style="bold bright_yellow")
    trial.add_column("DURING A TRIAL", style="bold white", no_wrap=True)
    trial.add_column("WHAT IT DOES", style="white")
    trial.add_row("hint", "Ask your ring for a hint (not every Lantern gets one)")
    trial.add_row("leave", "Walk away from the trial")

    console.print()
    console.print(Panel(commands, title="[bold bright_green]RING COMMANDS[/bold bright_green]",
                        border_style="bright_green", box=box.HEAVY, padding=(1, 2)))
    console.print(Panel(trial, border_style="bright_yellow", box=box.HEAVY, padding=(1, 2)))
    console.print(Align.center("[italic bright_black]Every command costs charge. Spend it wisely.[/italic bright_black]"))


OATH = [
    "Through the dark, I hold my will.",
    "Through despair, I hold my hope.",
    "Through fear, I hold my ground.",
    "And by the light I carry, I bring it home.",
]


def _recharge_bar():
    """Fill the ring's charge bar from empty to full."""
    with Live(console=console, refresh_per_second=20) as live:
        for percent in range(0, 101, 5):
            filled = percent // 5
            bar = "█" * filled + "░" * (20 - filled)
            live.update(Align.center(Text(f"CHARGE  [{bar}]  {percent:>3}%", style="bold bright_green")))
            if not FAST:
                time.sleep(0.08)


def won():
    """The ending: say the oath, recharge the ring, restore the battery."""
    scene("THE CHAMBER AWAKENS", "bright_green")
    line("The three lenses settle into the heart of the battery.", 0.025, "white", wait=0.8)
    line("The fault seals. A pulse of green light runs through the Chamber.", 0.025, "bright_green", wait=1)
    line("Your ring stirs. It is waiting for you to speak.", 0.03, "bright_white", wait=1.5)

    scene("THE OATH", "bright_green")
    for oath_line in OATH:
        type_text(oath_line, 0.05, "bold bright_green")
        pause(0.8)
    pause(0.5)

    console.print()
    _recharge_bar()
    pause(0.5)

    status_panel(
        "CHARGE: 100%\nCENTRAL BATTERY: RESTORED\nEMOTIONAL SPECTRUM: CONNECTED",
        title="RING STATUS", color="bright_green", box_style=box.DOUBLE,
    )
    pause(1.5)

    clear_screen()
    line("Across the cosmos, silent rings begin to glow.", 0.025, "white", wait=0.8)
    line("The light is home.", 0.05, "bold bright_green", wait=1.5)
    line("The trials have accepted you. What will you do with such power?", 0.03, "bright_white", wait=1.5)

    console.print(Align.center(Text("THANK YOU FOR PLAYING", style="bold bright_green")))
    console.print()


def lost():
    """The ending when the ring runs out of charge."""
    scene("THE LIGHT GOES OUT", "red")
    line("Your ring flickers. The last of its charge slips away.", 0.03, "yellow", wait=0.8)
    line("The constructs fade. The glow in your hand is gone.", 0.03, "white", wait=0.8)
    line("In the dark, the Central Power Battery is still broken.", 0.035, "bold red", wait=1.5)

    status_panel(
        "CHARGE: 0%\nCENTRAL BATTERY: CRITICAL\nMISSION: FAILED",
        title="RING STATUS", color="red",
    )
    pause(1.5)

    line("Somewhere, another Lantern is waiting for a chance.", 0.03, "bright_black", wait=1.5)
    console.print(Align.center(Text("GAME OVER", style="bold red")))
    console.print()


def view(result: str):
    print(result)



