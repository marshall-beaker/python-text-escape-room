rooms = {
    "bedroom": {
        "description": "You are in a bedroom. There is a desk with a drawer, a door to the north, and a door to the south.",
        "north": "hallway",
        "south": "kitchen",
    },
    "kitchen": {
        "description": "You are in a kitchen. There is a door to the north and a mysterious note on the wall.",
        "north": "bedroom",
    },
    "hallway": {
        "description": "You are in a hallway. There is a mirror on the wall with a picture on it, a locked door to the north, and a door to the east.",
        "south": "bedroom",
        "north": "exit",
        "east": "bathroom",
        "locked": True
    },
    "bathroom": {
        "description": "You are in a bathroom. There is a safe and a door to the hallway west.",
        "west": "hallway"
    },
    
    
    "exit": {
        "description": "You see the exit door. Freedom is close!"
    }
}

current_room = "bedroom"
inventory = []
digits = []