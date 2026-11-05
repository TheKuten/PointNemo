from rich import print
import time

class Wood:

    def __init__(self, qty:int=1):
        self.name = "Wood"
        self.qty = qty

    def use(self, player):
        print("[bright_blue]You inspect the Wood.[/bright_blue]")
        time.sleep(1)
        print(f"[bright_green]{player["name"]}: Well, beauty of nature.[/bright_green]")
        time.sleep(1)