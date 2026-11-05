from rich import print
import lib.chat as chat
import time

class HerbalPatch:

    def __init__(self, qty:int=1):
        self.name = "Herbal Patch"
        self.qty = qty
        self.req = {
            "Leaf": 10
        }
        self.consumable = True

    def use(self, player):
        if player["hp"] >= 100:
            print("[bright_blue]You have full HP.[/bright_blue]")
            time.sleep(1)
            return

        player["hp"] += 30
        if player["hp"] > 100: player["hp"] = 100
        print("[bright_blue]You applied the Herbal Patch.[/bright_blue] [yellow]+30 HP[/yellow]")
        time.sleep(1)
        if player["obj"] == "herbal":
            chat.play(23, player["name"])
            player["status"].append("sleep")
            player["obj"] = "sleep2"