from rich import print
import time

class Phone:

    def __init__(self, qty:int=1):
        self.name = "Phone"
        self.qty = qty

    def use(self, player):
        print("[bright_blue]There is no network...[/bright_blue]")
        time.sleep(1)
        print(f"[bright_green]{player["name"]}: (Sigh) No use, huh?[/bright_green]")
        time.sleep(1)