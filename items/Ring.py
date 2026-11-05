from rich import print
import time
import lib.chat as chat

class Ring:

    def __init__(self, qty:int=1):
        self.name = "Ring"
        self.qty = qty

    def use(self, player):
        print("[bright_blue]You inspect the ring on your finger.[/bright_blue]")
        time.sleep(1)

        if "ring" in player["status"]:
            print(f"[bright_green]{player["name"]}: I miss her...[/bright_green]")
            time.sleep(1)
            return
        
        chat.play(12, player["name"])
        player["status"].append("ring")
        time.sleep(1)