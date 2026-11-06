import lib.chat as chat
import lib.actions as act
import lib.cutscenes as cs
import os
import importlib
import pathlib
import sys
import random
import time
from rich import print

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

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

# Items Handler

items = {}

itemsPath = pathlib.Path("./Items")
sys.path.append(str(itemsPath.absolute()))

for filePath in itemsPath.glob("*.py"): # Searches a directory for files and folders that match a specific Unix shell-style wildcard pattern
    if filePath.name != "__init__.py":  # Skip package initialization files
        moduleName = filePath.stem
        module = importlib.import_module(moduleName)

        class_name = "".join(part.capitalize() for part in moduleName.split("_")) # Convert into PascalCase

        # Check if the class exists in the module
        if hasattr(module, class_name):
            items[class_name] = getattr(module, class_name)
        # Fallback: check for exact match with moduleName if not using PascalCase
        elif hasattr(module, moduleName):
            items[moduleName] = getattr(module, moduleName)

# Player dictionary can be modified to skip certain storyline

player = {
    "hp": 100,
    "inv": [items.get("Phone")(), items.get("Ring")()],
    "hunger": 10,
    "name": "YOU",
    "days": 1, # Default: 1
    "actions": 0,
    "obj": "search1", # Default: search1
    "items": items,
    "status": []
}

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def resetScene():
    clear()
    print("                       [Day {0}]                        ".format(player["days"]))
    print()
    print("\n".join(scene))
    if player["days"] == 1:
        chat.play(2, player["name"])
    elif player["days"] == 2:
        chat.play(11, player["name"])
        player["obj"] = "rock"

def prompt():
    print("HP: {0} | HUNGER: {1}".format(player["hp"], player["hunger"]))
    print("[S] SEARCH [H] HUNT [B] BAG", end="")
    if "sleep" in player["status"]: print("[yellow] [Z] SLEEP[/yellow]")
    else: print(" [Z] SLEEP")
    action = input(">> ")
    match action.lower():
        case "s" | "search":
            act.search(player)
        case "h" | "hunt":
            act.hunt(player)
        case "b" | "bag":
            act.bag(player)
        case "z" | "sleep":
            if not "sleep" in player["status"]:
                print(f"[bright_green]{player["name"]}: I'm not tired yet.[/bright_green]")
                time.sleep(1)
            else:
                player["status"].remove("sleep")
                match player["days"]:
                    case 1:
                        clear()
                        cs.Cutscene2(player)
                    case 2:
                        clear()
                        cs.Cutscene4(player)

                player["days"] += 1
                player["actions"] = 0
                resetScene()
        case "e" | "end":
            return
        case _:
            print("[bright_green]{}: I don't think I can do that. Let's try again.[/bright_green]".format(player["name"]))

    player["actions"] += 1

    # Hunger & Health System
    if random.random() > 0.5:
        player["hunger"] -= random.randint(1,2)
        if player["hunger"] < 0: player["hunger"] = 0
    if player["hunger"] <= 0:
        player["hp"] -= 10
        print("[bright_red]Hungry! -10 HP[/bright_red]")
    if player["hp"] <= 0:
        chat.play(18, player["name"])
        return

    prompt()

# Game starts
clear()

# Beginning Cutscene
cs.Cutscene1(player)

resetScene()
prompt()
