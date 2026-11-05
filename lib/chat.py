import json
import time
from rich import print

with open('lib/dialogues.json', 'r', encoding='utf-8') as file:
    dialogues = json.load(file)

def play(i: int, name:str = "YOU"):
    for line in dialogues[i]:
        print(line.format(name), end="")
        input("")