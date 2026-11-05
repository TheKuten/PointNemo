from rich import print
import lib.chat as chat

class Hut:

    def __init__(self, qty:int=1):
        self.name = "Hut"
        self.qty = qty
        self.req = {
            "Wood": 15
        }
        self.consumable = True

    def use(self, player):
        player["obj"] = "hunt"
        player["status"].append("canHunt")
        chat.play(6, player["name"])