from rich import print
import time

class Spear:

    def __init__(self, qty:int=1):
        self.name = "Spear"
        self.qty = qty
        self.req = {
            "Wood": 10,
            "Rock": 5
        }

    def use(self, player):
        print("[bright_blue]You inspect the Spear.[/bright_blue]")
        time.sleep(1)
        print(f"[bright_green]{player["name"]}: This will be handy for hunting.")
        time.sleep(1)