from classes.game import Person, BColors
from classes.magic import Spell
from classes.inventory import Item

# Create Black Magic
fire = Spell("Fire", 10, 100, "black")
thunder = Spell("Thunder", 10, 100, "black")
blizzard = Spell("Blizzard", 10, 100, "black")
meteor = Spell("Meteor", 20, 200, "black")
quake = Spell("Quake", 14, 140, "black")

# Create White Magic
cure = Spell("Cure", 12, 120, "white")
cura = Spell("Cura", 18, 200, "white")


# Create some Item

potion = Item("Potion", "potion", "Heals 50 HP", 50)
hipotion = Item("Hi-Potion", "potion", "Heals 100HP", 100)
superpotion = Item("Super Potion", "potion", "Heals 500 of HP", 500)
elixer = Item("Elixer", "elixer", "Fully restores HP/MP of one party member", 9999)
hielixer = Item("Mega Elixer", "elixer", "Fully restores party's HP/MP", 9999)

grenade = Item("Grenade", "attack", "Deals 500 damage", 500)

player_spells = [fire, thunder, blizzard, meteor, cure, cura]
player_items = [{"item": potion, "quantity": 15}, {"item": hipotion, "quantity": 5},
                {"item": superpotion, "quantity": 5}, {"item": elixer, "quantity": 5},
                {"item": hielixer, "quantity": 5}, {"item": grenade, "quantity": 1}]

player = Person(460, 65, 60, 34, player_spells, player_items)
enemy = Person(1200, 65, 45, 35, [], [])

running = True
i = 0

print(BColors.FAIL + BColors.BOLD + "AN ENEMY ATTACKS!" + BColors.ENDC)

while running:
    print("===================")
    player.choose_action()
    choice = input("Choose action: ")
    index = int(choice) - 1

    if index == 0:
        dmg = player.generate_damage()
        enemy.take_damage(dmg)
        print("\nYou attacked for" + BColors.BOLD, dmg, BColors.ENDC + "points of damage.")
    elif index == 1:
        player.choose_magic()
        magic_choice = int(input("Choose magic: ")) - 1

        if magic_choice == -1:
            continue

        spell = player.magic[magic_choise]
        magic_dmg = spell.generateDamage()

        current_mp = player.get_mp()

        if spell.cost > current_mp:
            print(BColors.FAIL + "\nNot enough MP\n" + BColors.ENDC)
            continue

        player.reduce_mp(spell.cost)

        if spell.type == "white":
            player.heal(magic_dmg)
            print(BColors.OKBLUE + "\n" + spell.name + " heals for", str(magic_dmg), "HP." + BColors.ENDC)
        elif spell.type == "black":
            enemy.take_damage(magic_dmg)
            print(BColors.OKBLUE + "\n" + spell.name + " deals", str(magic_dmg), "points of damage" + BColors.ENDC)
    elif index == 2:
        player.choose_item()
        item_choice = int(input("Choose items: ")) - 1

        if item_choice == -1:
            continue
        item = player.items[item_choice]["item"]

        if player.items[item_choice]["quantity"] == 0:
            print(BColors.FAIL + "\n" + "None left..." + BColors.ENDC)
            continue

        player.items[item_choice]["quantity"] -= 1

        if item.type == "potion":
            player.heal(item.prop)
            print(BColors.OKGREEN + "\n" + item.name + " heals for", str(item.prop), "HP" + BColors.ENDC)
        elif item.type == "elixer":
            player.hp = player.maxhp
            player.mp = player.maxmp
            print(BColors.OKGREEN + "\n" + item.name + " fully restore HP/MP" + BColors.ENDC)
        elif item.type == "attack":
            enemy.take_damage(item.prop)
            print(BColors.FAIL + "\n" + item.name + " deals", str(item.prop), "points of damage" + BColors.ENDC)

    enemy_choice = 1

    enemy_dmg = enemy.generate_damage()
    player.take_damage(enemy_dmg)
    print("Enemy attacks for" + BColors.BOLD, enemy_dmg, BColors.ENDC + "points of damage\n")

    print("===================\n")
    print("Enemy HP:", BColors.FAIL + str(enemy.get_hp()) + "/" + str(enemy.get_max_hp()) + BColors.ENDC + "\n")

    print("Your HP: " + BColors.OKGREEN + str(player.get_hp()) + "/" + str(player.get_max_hp()) + BColors.ENDC)
    print("Your MP: " + BColors.OKBLUE + str(player.get_mp()) + "/" + str(player.get_max_mp()) + BColors.ENDC + "\n")

    if enemy.get_hp() == 0:
        print(BColors.OKGREEN + "You win!" + BColors.ENDC)
        running = False
    elif player.get_hp() == 0:
        print(BColors.FAIL + "You enemy has defeated you!" + BColors.ENDC)
        running = False
