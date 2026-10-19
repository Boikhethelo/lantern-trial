import time
import os
import sys

from rich.console import Console
from rich.panel import Panel
from rich.align import Align
from rich.text import Text
from rich.rule import Rule
from rich import box

console = Console()

def clear_screen():
    console.clear()

def pause(seconds=1.5):
    time.sleep(seconds)

def type_text(text, delay=0.035, style="white"):
    """Print text character by character for cinematic narration."""
    for char in text:
        console.print(char, end="", style=style, markup=False, highlight=False)
        sys.stdout.flush()
        time.sleep(delay)
    console.print()


def slow_print(text, delay=0.06, style="white"):
    type_text(text, delay, style)


def dramatic_pause(seconds=2):
    pause(seconds)

def show_title():
    clear_screen()

    title = r"""
 _        ___    _   _ _____ ___ ___ _  _
| |      / _ \  | \ | |_   _|   \_ _| \| |
| |__   | (_) | |  \| | | | | |) | || .` |
|____|   \___/  |_|\__| |_| |___/___|_|\_|

              T H E   L A N T E R N   T R I A L S
"""

    console.print(
        Align.center(
            Text(title, style="bold bright_green"),
            vertical="middle"
        )
    )
    pause(2)

    console.print(
        Align.center(
            "[italic bright_white]When the universe goes dark, "
            "even the brightest must face the end.[/italic bright_white]"
        )
    )

    pause(3)


# ---------- THE STORY ----------

def opening_cinematic():
    show_title()
    clear_screen()

    console.print(Rule("[bold red]THE WAR OF LIGHT[/bold red]"))
    pause(1)

    type_text(
        "For eons, the light endured.\n",
        0.045,
        "bright_white"
    )
    pause(1)

    type_text(
        "Across the stars, Lanterns stood as guardians of will, "
        "hope, and the indomitable light that binds all things.\n",
        0.025,
        "white"
    )
    pause(2)

    type_text(
        "Then came the War of Light.\n",
        0.07,
        "bold red"
    )
    pause(1)

    type_text(
        "Worlds burned. Corps fell. The skies themselves became "
        "battlegrounds.\n",
        0.035,
        "red"
    )
    pause(1)

    type_text(
        "And at last... the war ended.\n",
        0.07,
        "bright_white"
    )
    pause(3)

    console.print()
    console.print(
        Panel(
            Align.center(
                Text(
                    "VICTORY WAS WON.\n"
                    "BUT THE LIGHT WAS NOT SAVED.",
                    style="bold white",
                    justify="center"
                ),
                vertical="middle"
            ),
            border_style="red",
            box=box.DOUBLE,
            padding=(1, 4)
        )
    )
    pause(3)

    clear_screen()
    console.print(Rule("[bold yellow]THE SILENCE[/bold yellow]"))
    pause(1)

    type_text(
        "Deep within the heart of the Lantern Corps stood "
        "the Central Power Battery...\n",
        0.04,
        "bright_yellow"
    )
    pause(2)

    type_text(
        "The source from which countless rings drew their power. "
        "The beacon that connected every Lantern to the light.\n",
        0.03,
        "white"
    )
    pause(2)

    type_text(
        "But in the aftermath of the war, something went wrong.\n",
        0.05,
        "yellow"
    )
    pause(2)

    type_text(
        "A fault tore through the battery's core.\n",
        0.06,
        "bold red"
    )
    pause(1)

    type_text(
        "Its light flickered...\n",
        0.09,
        "yellow"
    )
    pause(1)

    type_text(
        "And then it began to die.\n",
        0.09,
        "bold red"
    )
    pause(3)

    console.print()
    console.print(
        Panel(
            Align.center(
                Text(
                    "POWER FLOW: DISRUPTED\n"
                    "RING RECHARGING: OFFLINE\n"
                    "CENTRAL BATTERY: CRITICAL",
                    style="bold red",
                    justify="center"
                )
            ),
            title="[bold red]SYSTEM FAILURE[/bold red]",
            border_style="red",
            box=box.HEAVY
        )
    )
    pause(3)

    type_text(
        "\nOne by one, Lantern rings fell silent.\n",
        0.045,
        "white"
    )
    pause(1)

    type_text(
        "Across the cosmos, emerald constructs dissolved into dust. "
        "Signals vanished. Guardians lost their power.\n",
        0.025,
        "bright_black"
    )
    pause(2)

    type_text(
        "The Corps had survived the war...\n",
        0.05,
        "white"
    )
    pause(1)

    type_text(
        "Only to face extinction in its aftermath.\n",
        0.06,
        "bold red"
    )
    pause(3)


 # ---------- THE THREE LENSES ----------

    clear_screen()
    console.print(Rule("[bold bright_green]THE ONLY HOPE[/bold bright_green]"))
    pause(1)

    type_text(
        "Ancient records speak of a way to restore the flow of light.\n",
        0.035,
        "white"
    )
    pause(2)

    type_text(
        "Three legendary lenses. Three trials. Three tests "
        "of what it truly means to be a Lantern.\n",
        0.035,
        "bright_white"
    )
    pause(2)

    lenses = [
        (
            "LENS OF HOPE",
            "To believe that light can return, even when "
            "darkness seems absolute.",
            "bright_cyan"
        ),
        (
            "LENS OF WILL",
            "To stand unbroken when every instinct tells you "
            "to surrender.",
            "bright_green"
        ),
        (
            "LENS OF RESOLVE",
            "To press forward when the cost of continuing "
            "may be everything.",
            "bright_yellow"
        ),
    ]

    for name, description, color in lenses:
        console.print()
        console.print(
            Panel(
                Align.center(
                    Text.from_markup(
                        f"[bold {color}]{name}[/bold {color}]\n\n"
                        f"[italic white]{description}[/italic white]",
                        justify="center"
                    )
                ),
                border_style=color,
                box=box.DOUBLE,
                padding=(1, 3)
            )
        )
        pause(2)

    pause(1)

    type_text(
        "\nOnly by recovering all three can the damaged core "
        "be repaired.\n",
        0.035,
        "white"
    )
    pause(1)

    type_text(
        "Only then can the light flow again.\n",
        0.05,
        "bright_green"
    )
    pause(3)

 # ---------- THE PLAYER ----------

    clear_screen()
    console.print(Rule("[bold red]YOUR FINAL CHARGE[/bold red]"))
    pause(1)

    type_text(
        "And so, you stand at the threshold of the trials.\n",
        0.05,
        "white"
    )
    pause(2)

    type_text(
        "Your ring is all that remains between you "
        "and the darkness.\n",
        0.04,
        "white"
    )
    pause(2)

    type_text(
        "Its light is fading. Its reserves are nearly spent.\n",
        0.05,
        "yellow"
    )
    pause(2)

    type_text(
        "You have no sanctuary. No second charge. "
        "No guarantee of return.\n",
        0.04,
        "bright_red"
    )
    pause(2)

    type_text(
        "Every step will consume power.\n",
        0.06,
        "yellow"
    )
    pause(1)

    type_text(
        "Every trial will demand more.\n",
        0.06,
        "yellow"
    )
    pause(1)

    type_text(
        "And until the Central Power Battery is restored...\n",
        0.05,
        "white"
    )
    pause(2)

    type_text(
        "YOUR RING CANNOT RECHARGE.\n",
        0.08,
        "bold red"
    )
    pause(3)

    console.print()
    console.print(
        Panel(
            Align.center(
                Text(
                    "CHARGE REMAINING: CRITICAL\n"
                    "RECHARGING: IMPOSSIBLE\n"
                    "MISSION: RESTORE THE LIGHT",
                    style="bold bright_green",
                    justify="center"
                )
            ),
            title="[bold green]RING STATUS[/bold green]",
            border_style="bright_green",
            box=box.HEAVY,
            padding=(1, 3)
        )
    )
    pause(3)

    clear_screen()

    console.print(
        Align.center(
            Text(
                r"""
      .-=========-.
      \   .---.   /
       \  | * |  /
        \ '---' /
         '-----'
          / | \
         /  |  \
            |
            |
          __|__
        .'     '.
       /  TRIALS \
      '-----------'
""",
                style="bright_green"
            )
        )
    )

    pause(2)

    type_text(
        "The Corps does not need another hero who can win a war.\n",
        0.04,
        "white"
    )
    pause(2)

    type_text(
        "It needs someone who can bring the light home.\n",
        0.04,
        "bright_green"
    )
    pause(3)

    console.print()
    console.print(
        Align.center(
            Text(
                "THE LANTERN TRIALS BEGIN.",
                style="bold bright_green"
            )
        )
    )
    pause(2)

    console.print()
    console.input(
        "[bold white]Press ENTER to begin your trials...[/bold white]"
    )



def view_help():
    """TODO"""


def final():
    """TODO"""



def view(result:str):
    print(result)





