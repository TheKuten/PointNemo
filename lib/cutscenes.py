import lib.chat as chat
from rich import print
import sys
import time

gameName = [
    "██████╗  ██████╗ ██╗███╗   ██╗████████╗    ███╗   ██╗███████╗███╗   ███╗██████╗ ",
    "██╔══██╗██╔═══██╗██║████╗  ██║╚══██╔══╝    ████╗  ██║██╔════╝████╗ ████║██╔═══██╗",
    "██████╔╝██║   ██║██║██╔██╗ ██║   ██║       ██╔██╗ ██║█████╗  ██╔████╔██║██║   ██║",
    "██╔═══╝ ██║   ██║██║██║╚██╗██║   ██║       ██║╚██╗██║██╔══╝  ██║╚██╔╝██║██║   ██║",
    "██║     ╚██████╔╝██║██║ ╚████║   ██║       ██║ ╚████║███████╗██║ ╚═╝ ██║╚██████╔╝",
    "╚═╝      ╚═════╝ ╚═╝╚═╝  ╚═══╝   ╚═╝       ╚═╝  ╚═══╝╚══════╝╚═╝     ╚═╝ ╚═════╝ ",
]

scene = [
    "[yellow]                      \\   |   /                      [/yellow]",
    "[yellow]                   --   ( ☼ )   --                   [/yellow]",
    "[yellow]                      /   |   \\                      [/yellow]",
    "        v                                 v          ",
    "                   v            v                    ",
    "[green]                     _  /\\ _                         [/green]",
    "[green]                   /  \\/  \\  \\                       [/green]",
    "[green]                 /  🌴  🌴  🌴 \\                      [/green]",
    "[yellow]~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~[/yellow]",
    "[blue]  ~       ~       ~       ~       ~       ~       ~  [/blue]",
    "[blue]      ~       ~       ~       ~       ~       ~      [/blue]",
    "[blue]  ~       ~       ~       ~       ~       ~       ~  [/blue]",
]

nightScene = [
    "[bold yellow]/\\===============================================================/\\ [/bold yellow]",
    "[bold yellow]\\ \\ [/bold yellow][dim cyan]                        *       .       *                   [/dim cyan][bold yellow]/ /[/bold yellow]",
    "[bold yellow] \\ \\-----------------------------------------------------------/ / [/bold yellow]",
    "[bold yellow]  \\ \\ [/bold yellow][dim cyan]      .           *         [/dim cyan][bold bright_white](  🌖  )[/bold bright_white][dim cyan]       .       *    [/dim cyan][bold yellow]/ /  [/bold yellow]",
    "[bold yellow]   \\ \\_______________________________________________________/ /   [/bold yellow]",
    "[bold yellow]   |  |====================================================|  |   [/bold yellow]",
    "[bold yellow]   |  |[/bold yellow][dim cyan]   .       *       .       .       *       .      . [/dim cyan][bold yellow]|  |   [/bold yellow]",
    "[bold yellow]   |  |[/bold yellow][dim cyan]       *           .        *            .          [/dim cyan][bold yellow]|  |   [/bold yellow]",
    "[bold yellow]   |  |[/bold yellow][dim cyan]   .            [/dim cyan][bold red]( 🔥 )[/bold red][dim cyan]                     .        [/dim cyan][bold yellow]|  |   [/bold yellow]",
    "[bold yellow]   |  |_______________/  ||  \\_____________________________|  |   [/bold yellow]",
    "[bold yellow]   |  |____________________________________________________|  |   [/bold yellow]",
    "[bold yellow]   |  |                                                    |  |   [/bold yellow]",
    "[bold yellow]   |  |                                                    |  |   [/bold yellow]",
    "[bold yellow]   |__|____________________________________________________|__|   [/bold yellow]",
    "[green]  /                                                              \\ [/green]",
    "[dim green] /     . . . . . . . . . . . . . . . . . . . . . . . . . . . .    \\ [/dim green]",
    "[green]/                                                                  \\ [/green]",
    "[dim green]|   .    .   .  _ .   .   ..     .    .   .   .  _ .   .   ..      |[/dim green]",
    "[green]|  .   _   .   / \\ .    .    .  .   _   .    / \\ .    .    .       |[/green]",
    "[green]|     / \\     |   |   .   .        / \\      |   |   .   .          |[/green]",
    "[bold green]|____|___|____|___|_______________|___|_____|___|__________________|[/bold green]",
]

SOSScene = [
    "[bold yellow]                          \\       |       /                        [/bold yellow]",
    "[bold yellow]                           \\  [bold bright_yellow]  ( ☼ )  [/bold bright_yellow]  /                         [/bold yellow]",
    "[bold yellow]                        -----  -- --  -----                        [/bold yellow]",
    "[bold yellow]                           /     |     \\                           [/bold yellow]",
    "[dim cyan]        v                                         v                [/dim cyan]",
    "[dim cyan]                   v                v                              [/dim cyan]",
    "[bold green]        🌴                                               🌴        [/bold green]",
    "[bold bright_cyan]~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~[/bold bright_cyan]",
    "[bold blue]  ~       ~       ~       ~       ~       ~       ~       ~       ~[/bold blue]",
    "[bold blue]      ~       ~       ~       ~       ~       ~       ~       ~      [/bold blue]",
    "[bold blue]  ~       ~       ~       ~       ~       ~       ~       ~       ~[/bold blue]",
    "[bold yellow]-------------------------------------------------------------------[/bold yellow]",
    "[yellow]  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . [/yellow]",
    "[yellow] /     . . . . . . . . . . . . . . . . . . . . . . . . . . . .     \\ [/yellow]",
    "[yellow]/                                                                  \\ [/yellow]",
    "[yellow]|                                                                  |[/yellow]",
    "[yellow]|  [bold white]                     ___  ___  ___             [/bold white]                 |[/yellow]",
    "[yellow]|  [bold white]                    / __|/ _ \\/ __|           [/bold white]                  |[/yellow]",
    "[yellow]|  [bold white]                    \\__ \\ (_) \\__ \\        [/bold white]                     |[/yellow]",
    "[yellow]|  [bold white]                    |___/\\___/|___/           [/bold white]                  |[/yellow]",
    "[yellow]|                                                                  |[/yellow]",
    "[yellow]|   .    .   .  _ .   .   ..     .    .   .   .  _ .   .   ..      |[/yellow]",
    "[yellow]|  .   _   .   / \\ .    .    .  .   _   .    / \\ .    .    .       |[/yellow]",
    "[yellow]|_____/_\\_____|___|_______________|___|_____|___|__________________|[/yellow]",
]

burningHutScene = [
    "[bold red]                     🔥      🔥   🔥      🔥                       [/bold red]",
    "[bold bright_red]                 (  🔥  )  ( 🔥  )  (  🔥  )                   [/bold bright_red]",
    "[bold yellow]/\\================================================================/ \\ [/bold yellow]",
    "[bold red]\\ \\ [/bold red][bold yellow]                    🔥       🔥      🔥                  [/bold yellow][bold red]/ /[/bold red]",
    "[bold yellow] \\ \\------------------------------------------------------------/ / [/bold yellow]",
    "[bold yellow]  \\ \\ [/bold yellow][bold red]     ( 🔥 )       [/bold red][bold bright_yellow]( ☼ )[/bold bright_yellow][bold red]       ( 🔥 )           [/bold red][bold yellow]/ /  [/bold yellow]",
    "[bold yellow]   \\ \\_______________________________________________________/ /   [/bold yellow]",
    "[bold yellow]   |  |====================================================|  |   [/bold yellow]",
    "[bold yellow]   |  |[/bold yellow][bold green]  🌴 [/bold green][dim cyan] .       *       .       .       *    [/dim cyan][bold green]🌴  [/bold green][bold yellow]|  |   [/bold yellow]",
    "[bold yellow]   |  |[/bold yellow][bold red]      🔥      [/bold red][bold bright_cyan]~~~~~~~~~~~~~~~~~~~[/bold bright_cyan][bold red]     🔥         [/bold red][bold yellow]|  |   [/bold yellow]",
    "[bold yellow]   |  |[/bold yellow][bold red]    ( 🔥 )   [/bold red][bold blue]  ~       ~       ~  [/bold blue][bold red]  ( 🔥 )       [/bold red][bold yellow]|  |   [/bold yellow]",
    "[bold yellow]   |  |_______________/[bold red]  ||  ||  ||  [/bold red]\\_____________________|  |   [/bold yellow]",
    "[bold yellow]   |  |____________________________________________________|  |   [/bold yellow]",
    "[bold yellow]   |  |                                                    |  |   [/bold yellow]",
    "[bold yellow]   |__|____________________________________________________|__|   [/bold yellow]",
    "[yellow]  /   .   .   .   [bold red]🔥🔥🔥[/bold red]  .   .   .   .   .   .   .   .   .   \\ [/yellow]",
    "[yellow] /     . . . . . . . . . . . . . . . . . . . . . . . . . . . .    \\ [/yellow]",
    "[yellow]/                                                                 \\ [/yellow]",
    "[yellow]|                      [bold white]___  ___  ___[/bold white]                              |[/yellow]",
    "[yellow]|                     [bold white]/ __|/ _ \\/ __|[/bold white]                             |[/yellow]",
    "[yellow]|                     [bold white]\\__ \\ (_) \\__ \\ [/bold white]                            |[/yellow]",
    "[yellow]|                     [bold white]|___/\\___/|___/[/bold white]                             |[/yellow]",
    "[yellow]|                                                                  |[/yellow]",
    "[yellow]|   .    .   .  _ .   .   ..     .    .   .   .  _ .   .   ..      |[/yellow]",
    "[yellow]|_____/_\\_____|___|_______________|___|_____|___|__________________|[/yellow]",
]

ending1 = [
    "[bold green]██████╗ ███╗   ██╗██████╗ ██╗███╗   ██╗██████╗       ██╗[/bold green]",
    "[bold green]██╔════╝████╗  ██║██╔══██╗██║████╗  ██║██╔════╝     ███║[/bold green]",
    "[bold green]█████╗  ██╔██╗ ██║██║  ██║██║██╔██╗ ██║██║  ███╗    ╚██║[/bold green]",
    "[bold green]██╔══╝  ██║╚██╗██║██║  ██║██║██║╚██╗██║██║   ██║     ██║[/bold green]",
    "[bold green]███████╗██║ ╚████║██████╔╝██║██║ ╚████║╚██████╔╝     ██║[/bold green]",
    "[bold green]╚══════╝╚═╝  ╚═══╝╚═════╝ ╚═╝╚═╝  ╚═══╝ ╚═════╝      ╚═╝[/bold green]",
    "[bold green]           Those Who Were Never Meant to Leave          [/bold green]"
]

ending2 = [
    "[bold red]██████╗ ███╗   ██╗██████╗ ██╗███╗   ██╗██████╗      ██████╗ [/bold red]",
    "[bold red]██╔════╝████╗  ██║██╔══██╗██║████╗  ██║██╔════╝     ╚════██╗[/bold red]",
    "[bold red]█████╗  ██╔██╗ ██║██║  ██║██║██╔██╗ ██║██║  ███╗     █████╔╝[/bold red]",
    "[bold red]██╔══╝  ██║╚██╗██║██║  ██║██║██║╚██╗██║██║   ██║    ██╔═══╝ [/bold red]",
    "[bold red]███████╗██║ ╚████║██████╔╝██║██║ ╚████║╚██████╔╝    ███████╗[/bold red]",
    "[bold red]╚══════╝╚═╝  ╚═══╝╚═════╝ ╚═╝╚═╝  ╚═══╝ ╚═════╝     ╚══════╝[/bold red]",
    "[bold red]                  Wrong Place, Wrong Time                   [/bold red]"
]

def Cutscene1(player):
    print("\n".join(gameName))
    print("\n".join(scene))
    chat.play(0, player["name"])

    def askName():
        name = input("What is your name? >> ").strip().upper()
        if not name:
            print("[bright_magenta]MEMEY: C'mon, don't be shy. I already told you my name.")
            time.sleep(1)
            return askName()
        player["name"] = name

    askName()
    chat.play(1, player["name"])
    input("Take her hand [ENTER] >> ")

def Cutscene2(player):
    print("\n".join(nightScene))
    chat.play(10, player["name"])
    input("Sleep back [ENTER] >> ")

def Cutscene3(player):
    player["hp"] -= 43

    existingPatch = next((i for i in player["inv"] if i.name == "Herbal Patch"), None)
    if existingPatch:
        player["inv"][player["inv"].index(existingPatch)].qty += 1
    else:
        player["inv"].append(player["items"].get("HerbalPatch")(1))

    print("\n".join(SOSScene))
    chat.play(20, player["name"])
    input("Strike the snake with your Spear [ENTER] >> ")
    chat.play(21, player["name"])
    input("Twist your Spear to fatally damage the snake [ENTER] >> ")
    chat.play(22, player["name"])
    print("[bright_blue]You can CRAFT a Herbal Patch with 10 Leaves. Heals 30 HP.[/bright_blue]")
    time.sleep(1)

def Cutscene4(player):
    chat.play(24, player["name"])
    print("\n".join(burningHutScene))
    chat.play(25, player["name"])
    input("Comfort her [ENTER] >> ")
    chat.play(26, player["name"])

    def promptEnding():
        print("Save her [A] | Run [B]")
        option = input("Make a choice >> ").strip().lower()
        match option:
            case "a":
                chat.play(27, player["name"])
                input("Lift the log [ENTER] >> ")
                chat.play(28, player["name"])
                input("Use all your strength [ENTER] >>")
                chat.play(29, player["name"])
                print()
                print("\n".join(ending1))
                time.sleep(1)
                print("\nThanks for playing! Did you get Ending 2 yet?")
                time.sleep(1)
                input("EXIT [ENTER] >> ")
                sys.exit()
            case "b":
                chat.play(30, player["name"])
                print()
                print("\n".join(ending2))
                time.sleep(1)
                print("\nThanks for playing! Did you get Ending 1 yet?")
                time.sleep(1)
                input("EXIT [ENTER] >> ")
                sys.exit()
            case _:
                print("Invalid choice. [A/B]")
                promptEnding()

    promptEnding()
