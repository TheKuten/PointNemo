from rich import print
import lib.chat as chat
import random
import time

events = [
    {
        "desc": "You found Wood on the ground.",
        "item": "Wood"
    },
    {
        "desc": "You picked up some Leaves.",
        "item": "Leaf"
    },
    {
        "desc": "You collected some Rocks.",
        "item": "Rock"
    }
]

hunts = [
    {
        "desc": "You caught some fishes.",
        "item": "Fish"
    }
]

def search(player: dict):
    def searchAct(id:int=random.randint(0, len(events)-1)):
        amt = random.randint(3,10)
        selected = events[id]

        item = next((i for i in player["inv"] if i.name == selected["item"]), None)
        if item:
            player["inv"][player["inv"].index(item)].qty += amt
        else:
            player["inv"].append(player["items"].get(selected["item"])(amt))

        print(f"[bright_blue]{selected["desc"]}[/bright_blue] [yellow]+{amt}[/yellow]")

    # Storyline Events 

    if player["obj"] == "search1":
        searchAct(0)
        time.sleep(1)
        chat.play(3, player["name"])
        player["obj"] = "search2"
    elif player["obj"] == "search2":
        searchAct(0)
        wood = next((i for i in player["inv"] if i.name == "Wood"), None)
        if wood.qty >= 15:
            time.sleep(1)
            chat.play(4, player["name"])
            player["obj"] = "shelter"
    else:
        searchAct()
        time.sleep(1)
        if not "spear" in player["status"] and player["obj"] == "rock":
            rock = next((i for i in player["inv"] if i.name == "Rock"), None)
            wood = next((i for i in player["inv"] if i.name == "Wood"), None)
            if rock and wood and wood.qty >= 10 and rock.qty >= 5:
                player["status"].append("spear")
                chat.play(13, player["name"])
        elif not "sos" in player["status"] and player["obj"] == "sos":
            rock = next((i for i in player["inv"] if i.name == "Rock"), None)
            leaf = next((i for i in player["inv"] if i.name == "Leaf"), None)
            if rock and leaf and leaf.qty >= 15 and rock.qty >= 15:
                player["status"].append("sos")
                chat.play(17, player["name"])


def hunt(player: dict):
    def huntAct(id:int=random.randint(0, len(hunts)-1)):
        spear = next((i for i in player["inv"] if i.name == "Spear"), None)
        if not "canHunt" in player["status"] and not spear:
            print(f"[bright_green]{player["name"]}: Maybe I shouldn't be hunting yet.[/bright_green]")
            return
        
        if player["obj"] == "hunt":
            player["inv"].append(player["items"].get("Fish")(1))
            chat.play(7, player["name"])
            player["obj"] = "fish"
            player["status"].remove("canHunt")
            return
        
        amt = random.randint(3,10)
        selected = hunts[id]

        item = next((i for i in player["inv"] if i.name == selected["item"]), None)
        if item:
            player["inv"][player["inv"].index(item)].qty += amt
        else:
            player["inv"].append(player["items"].get(selected["item"])(amt))

        print(f"[bright_blue]{selected["desc"]}[/bright_blue] [yellow]+{amt}[/yellow]")

    # Storyline Events 

    if player["obj"] == "food":
        huntAct(0)
        time.sleep(1)
        chat.play(3, player["name"])
        player["obj"] = "sleep"
    elif player["obj"] == "fish2" and not "huntFish" in player["status"]:
        huntAct(0)
        player["status"].append("huntFish")
        time.sleep(1)
        chat.play(15, player["name"])
        time.sleep(1)
    else:
        huntAct()
        time.sleep(1)

recipes = [
    "[yellow]15x Wood: Hut[/yellow]",
    "[yellow]10x Wood + 5x Rock: Spear[/yellow]",
    "[yellow]15x Rock + 15x Leaf: SOS[/yellow]",
    "[yellow]10x Leaf: Herbal Patch[/yellow]"
]
    
def bag(player: dict):
    def prompt():
        print("="*29)
        print("             BAG             ")
        print("-"*29)
        if not player["inv"]:
            print("(Your inventory is empty)")
        else:
            for i,v in enumerate(player["inv"]):
                print(f"[{i+1}]: {v.name} (x{v.qty})")
        print("-"*29)
        print("[B] BACK [U] USE [C] CRAFT")
        print("="*29)

        action = input("BAG >> ").strip().lower()
        match action:
            case "b" | "back":
                return
            
            case "u" | "use":
                chosen = input("Which item would you like to use? >> ").strip().lower()

                if chosen.isdigit():
                    idx = int(chosen) - 1
                    if 0 <= idx < len(player["inv"]):
                        item = player["inv"][idx]
                    else:
                        item = None
                else:
                    item = next((f for f in player["inv"] if f.name.lower() == chosen), None)

                if not item:
                    print("No item found. Please try again.")
                    prompt()
                else:
                    item.use(player)
                    if hasattr(item, "consumable"):
                        player["inv"][player["inv"].index(item)].qty -= 1
                        if player["inv"][player["inv"].index(item)].qty <= 0:
                            player["inv"].pop(player["inv"].index(item))
                    prompt()

            case "c" | "craft":
                craftable = []
                print("="*29)
                print("            CRAFT            ")
                print("-"*29)

                # Unlockable Recipes

                for itemName, itemClass in player["items"].items():
                    testItem = itemClass()

                    if not hasattr(testItem, "req"): continue
                    if itemName == "Hut" and player["obj"] != "shelter": continue
                    if itemName == "Spear" and player["obj"] != "rock": continue
                    if itemName == "SOS" and player["obj"] != "sos": continue

                    passed = 0

                    for name, qty in testItem.req.items():
                        existing = next((i for i in player["inv"] if i.name == name), None)
                        if existing and existing.qty >= qty:
                            passed += 1

                    if passed == len(testItem.req):
                        craftable.append(itemName)
                        print(f"[{len(craftable)}]: {testItem.name}")        

                if not craftable: print("No craftables.")
                print("-"*29)
                print("[B] BACK | [C] CRAFT\n[V] VIEW RECIPES")
                print("="*29)

                def promptCraft():
                    if not craftable:
                        print("You have no craftables.")
                        return promptCMenu()

                    crafted = input("Enter the number/name of the craftable >> ").strip().lower()

                    if crafted == "b" or crafted == "back": return

                    if crafted.isdigit():
                        idx = int(crafted) - 1
                        if 0 <= idx < len(craftable):
                            item = craftable[idx]
                        else:
                            item = None
                    else:
                        item = next((f for f in craftable if f.lower() == crafted), None)

                    if not item:
                        print("No craftable found. Please try again.")
                        promptCraft()
                        return

                    craftedClass = player["items"].get(item)(1)

                    for name, qty in craftedClass.req.items():
                        existing = next((i for i in player["inv"] if i.name == name), None)
                        player["inv"][player["inv"].index(existing)].qty -= qty
                        if player["inv"][player["inv"].index(existing)].qty <= 0:
                            player["inv"].pop(player["inv"].index(existing))

                    exCrafted = next((i for i in player["inv"] if i.name == craftedClass.name), None)
                    
                    if exCrafted:
                        player["inv"][player["inv"].index(exCrafted)].qty += 1
                    else:
                        player["inv"].append(craftedClass)

                    print(f"[bright_blue]Crafted {craftedClass.name}[/bright_blue] [yellow]+1[/yellow]")
                    time.sleep(1)

                    # QTEs
                    if craftedClass.name == "Hut":
                        chat.play(5, player["name"])
                        player["obj"] = "placeHut"
                    elif craftedClass.name == "Spear":
                        chat.play(14, player["name"])
                        player["obj"] = "fish2"
                    elif craftedClass.name == "SOS":
                        chat.play(19, player["name"])
                        player["obj"] = "placeSOS"

                def promptCMenu():
                    cAction = input("CRAFT >> ").strip().lower()
                    match cAction:
                        case "b" | "back":
                            return
                        case "c" | "craft":
                            promptCraft()
                        case "v" | "view" | "view recipes":
                            print("\n".join(recipes))
                            promptCMenu()
                        case _:
                            print("No such crafting action. Please try again.")
                            promptCMenu()


                promptCMenu()
                prompt()

            case _:
                print("No such action. Please try again.")
                prompt()

    prompt()
