from character import Character
from item import Item
from area import Area
from monster import Monster
from game import explore

def main():
    print("Welcome to the Fantasy Game!")
    player_name = input("Enter your character's name: ")
    player = Character(name=player_name, health=100, attack=20, defense=10)

    # Add starting items
    player.add_item(Item(name="Health Potion", health_bonus=20))
    player.add_item(Item(name="Sword", attack_bonus=10))

    # Create areas
    forest = Area(name="Enchanted Forest", description="A mystical forest filled with ancient trees and magical creatures.")
    cave = Area(name="Dark Cave", description="A damp, dark cave that echoes with the sounds of unknown creatures.")

    # Add monsters and items to areas
    forest.add_monster(Monster(name="Wolf", health=40, attack=10, defense=5))
    forest.add_item(Item(name="Shield", defense_bonus=5))
    cave.add_monster(Monster(name="Bat", health=20, attack=5, defense=2))
    cave.add_item(Item(name="Magic Stone", health_bonus=10))

    # Main game loop
    areas = [forest, cave]
    while player.is_alive():
        print("\nWhat would you like to do?")
        print("1. Explore an area")
        print("2. Check inventory")
        print("3. Use an item")
        print("4. Quit")

        choice = input("Enter your choice: ")
        if choice == "1":
            print("Where would you like to explore?")
            for i, area in enumerate(areas):
                print(f"{i+1}. {area.name}")

            area_choice = int(input("Enter the number of the area: ")) - 1
            if 0 <= area_choice < len(areas):
                explore(player, areas[area_choice])
            else:
                print("Invalid choice. Please try again.")
        elif choice == "2":
            print("Inventory:")
            for item in player.inventory:
                print(f"{item.name} (Health Bonus: {item.health_bonus}, Attack Bonus: {item.attack_bonus}, Defense Bonus: {item.defense_bonus})")
        elif choice == "3":
            item_name = input("Enter the name of the item to use: ")
            player.use_item(item_name)
        elif choice == "4":
            print("Thank you for playing!")
            break
        else:
            print("Invalid choice. Please try again.")

        if not player.is_alive():
            print("You have been defeated. Game over.")

if __name__ == "__main__":
    main()
