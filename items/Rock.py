from rich import print
import lib.chat as chat
import time

class Rock:

    def __init__(self, qty:int=1):
        self.name = "Rock"
        self.qty = qty

    def use(self, player):
        print("[bright_blue]You inspect the Rock.[/bright_blue]")
        time.sleep(1)
        print(f"[bright_green]{player["name"]}: That is one rock solid rock.[/bright_green]")
        time.sleep(1)