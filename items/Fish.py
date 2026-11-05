from rich import print
import lib.chat as chat
import time

class Fish:

    def __init__(self, qty:int=1):
        self.name = "Fish"
        self.qty = qty
        self.consumable = True

    def use(self, player):
        if not "ateFish" in player["status"] and player["days"] == 1:
            chat.play(8, player["name"])
            player["status"].append("ateFish")
        elif player["hunger"] >= 10:
            print("[bright_blue]You are not hungry yet.[/bright_blue]")
            return
        else:
            print("[bright_magenta]MEMEY: And... it's ready! Here you go.[/bright_magenta]")
            time.sleep(1)

        player["hunger"] += 5
        if player["hunger"] > 10: player["hunger"] = 10
        print("[bright_blue]You ate the Fish cooked by MEMEY.[/bright_blue] [yellow]+5 Hunger[/yellow]")
        time.sleep(1)
        if player["obj"] == "fish":
            chat.play(9, player["name"])
            player["status"].append("sleep")
        elif player["obj"] == "fish2" and "huntFish" in player["status"]:
            chat.play(16, player["name"])
            print("[bright_blue]HUNGER SYSTEM\nYou have a chance to lose a random amount of hunger after each action.\nYour HP will start dropping when your hunger reaches 0.\nPay attention to your hunger and hunt for food to survive.[/bright_blue]")
            player["obj"] = "sos"
