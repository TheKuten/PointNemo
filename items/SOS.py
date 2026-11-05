from rich import print
import lib.chat as chat
import lib.cutscenes as cs

class SOS:

    def __init__(self, qty:int=1):
        self.name = "SOS"
        self.qty = qty
        self.req = {
            "Rock": 15,
            "Leaf": 15
        }
        self.consumable = True

    def use(self, player):
        player["obj"] = "herbal"
        cs.Cutscene3(player)