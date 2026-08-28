""" Final Project Code:

Escape Room Code

Author: Marshall Beaker (mhb25@calvin.edu)

Acknowledgements:
I used ChatGPT for help with brainstorming, understanding concepts, and image generation.
I also received help from my hockey teammate Alim Darmenov.

"""

import game_data
import os

def show_instructions():
    """Displays game instructions at the start"""
    print("Welcome to the Escape Room Game!")
    print("Your goal is to escape by exploring rooms, looking at objects, and solving puzzles.")
    print("If you need a reminder of the instructions say...show instructions...")
    print("You might want a notebook and pen!\n")
    
    print("Commands:")
    print("  go north / south / east / west")
    print("  look desk")
    print("  solve desk")
    print("  look mirror")
    print("  solve mirror")
    print("  look note")
    print("  solve note")
    print("  open safe")
    print("  use key")
    print("  digits")
    print("  inventory")
    print("  quit\n")

    input("Press Enter to start...")

def show_image(filename):
    """Opens an image file"""
    try:
        os.startfile(filename)
    except:
        print("Could not open image.")

def solve_cipher():
    """Solve the cipher puzzle"""

    answer = input("Decode the message: ").lower()

    print()

    if answer == "hello":
        if "5" not in game_data.digits:
            print("_"*30) 
            print("\n")
            print("Correct! You found the number 5.")
            game_data.digits.append("5")
        else:
            print("You already solved this puzzle.")
    else:
        print("Wrong answer.")
    
    print()

def solve_puzzle():
    """Solve the spot the difference puzzle"""

    answer = input("How many differences are there?: ").lower()

    print()

    if answer == "7":
        if "7" not in game_data.digits:
            print("_"*30)
            print("\n")
            print("Correct! You found the number 7.")
            game_data.digits.append("7")
        else:
            print("You already solved this puzzle.")
    else:
        print("Wrong answer.")
    
    print()

def solve_note():
    """Solve the note riddle puzzle"""
    
    answer = input("What has keys but no locks, space but no room, and you can enter but can't go inside?: ").lower()
    
    print()
    
    if answer == "keyboard":
        if "3" not in game_data.digits:
            print("_"*30)
            print("\n")
            print("Correct! You found the number 3.")
            game_data.digits.append("3")
        else:
            print("You already solved this puzzle.")
    else:
        print("Wrong answer.")

    print()

def show_room():
    room = game_data.rooms[game_data.current_room]
    
    print("_"*30)
    print()
    
    # Show room description
    print(room["description"])

    # Show item in a room 
    if "item" in room:
        print("You see a", room["item"])

    # Show directions
    directions = []
    for key in room:
        if key in ["north", "south", "east", "west"]:
            directions.append(key)

    if directions:
        print("Exits:", ", ".join(directions))
    
    print() # This line is for spacing to be visually apealing

def move_player(direction):
    """ Move player to a new room based on direction """

    current = game_data.current_room
    room = game_data.rooms[current]

    if direction in room:
    
        if current == "hallway" and direction == "north":
            if room.get("locked", False):
                print("The door is locked. You need a key.")
                return
    
        game_data.current_room = room[direction]
        print("You move to the", direction)
        print() # For spacing
    else:
        print("You can't go that way.")
        print()
    if game_data.current_room == "exit":
        print("You escaped! 🎉 Congratulations!")
        exit()
    
def take_item(item): #Do I need this anymore?
    """ Pick up an item """
    room = game_data.rooms[game_data.current_room]
    
    if "item" in room and room["item"] == item:
        game_data.inventory.append(item)
        del room["item"]
        print("You picked up the", item + ".")
        print() # For spacing 
    else:
        print("That item is not here.")

def show_inventory():
    """ Show what the player has in their inventory """
    
    if game_data.inventory:
        print("You have:", ", ".join(game_data.inventory))
        print() # For spacing
    else:
        print("Your inventory is empty.")
        
def use_item(item):
    """ Use an item """

    if item in game_data.inventory:
        if item == "key" and game_data.current_room == "hallway":
            game_data.rooms["hallway"]["locked"] = False
            print("You unlocked the door!")
            print()
        else:
            print("You can't use that here.")
            print()
    else:
        print("You don't have that item.")
        print()

def open_safe():
    """ Open safe using collected digits """
    
    if len(game_data.digits) < 3:
        print(" You don't have all of the numbers yet.")
        print()
        return
    
    code = input("Enter the code: ")
    print("_"*30)
    print ()
    
    correct_code = "".join(sorted(game_data.digits)) # "" empty string, join in a list, sort low to high from game digits
    
    if code == correct_code:
        print()
        print("The safe clicks open! Inside, you find a key.")
        
        # Only add key once
        if "key" not in game_data.inventory:
            game_data.inventory.append("key")
    else:
        print("Wrong code. The safe remains locked.")
    
    print()

def process_command(command):
    """ Process player commands """

    print("_"*30)
    print()
    print()# These three lines are for spacing to be visually apealing

    if command == "quit":
        print("Thanks for playing!")
        exit()
    
    elif command.startswith("go "):
        direction = command.split()[1]
        move_player(direction)
    
    elif command.startswith("take "):
        item = command.split()[1]
        take_item(item)
        
    elif command == "inventory":
        show_inventory()
    
    elif command.startswith("use "):
        item = command.split()[1]
        use_item(item)
        
    elif command == "look desk":
        if game_data.current_room == "bedroom":
            print("You open the drawer and find two strange notes...")
            print()

            show_image("cipher_key.png")
            show_image("cipher_puzzle.png")

        else:
            print("There is no desk here.")
            print()
    
    elif command == "solve desk":
        if game_data.current_room == "bedroom":
            solve_cipher()
        else:
            print("Nothing to solve here.")
            print()
    
    elif command == "look mirror":
        if game_data.current_room == "hallway":
            print("You find a strange picture in the mirror...Can you spot the differences?")
            print()

            show_image("mirror_puzzle.png")

        else:
            print("There is no mirror here.")
            print()
    
    elif command == "solve mirror":
        if game_data.current_room == "hallway":
            solve_puzzle()
        else:
            print("Nothing to solve here.")
            print()

    elif command == "open safe":
        if game_data.current_room == "bathroom":
            open_safe()
        else:
            print("There is no safe here.")
            print()

    elif command == "look note":
        if game_data.current_room == "kitchen":
            print("You find a mysterious note with a riddle...\n \nWhat has keys but no locks, space but no room, and you can enter but can't go inside? ")
            print()

        else:
            print("There is no note here.")
            print()

    elif command == "solve note":
        if game_data.current_room == "kitchen":
            solve_note()
        else:
            print("Nothing to solve here.")
            print()
    
    elif command == "digits":
        if game_data.digits:
            print("You have found these numbers:", ", ".join(sorted(game_data.digits)))
            print()

        else:
            print("You haven't found any numbers yet.")
            print()
    
    elif command == "show instructions":
        show_instructions()
    
    else:
        print("I don't understand that command.")
        print()
        
show_instructions()

while True:
    show_room()
    command = input("> ").lower()
    process_command(command)