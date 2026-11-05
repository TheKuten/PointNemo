from rich import print
import lib.chat as chat
import time

class Leaf:

    def __init__(self, qty:int=1):
        self.name = "Leaf"
        self.qty = qty

    def use(self, player):
        print("[bright_blue]You inspect the Leaf.[/bright_blue]")
        time.sleep(1)
        print(f"[bright_green]{player["name"]}: If only it had Nasi Lemak on top.[/bright_green]")
        time.sleep(1)