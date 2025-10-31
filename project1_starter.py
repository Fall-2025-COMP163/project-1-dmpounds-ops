"""
COMP 163 - Project 1: Character Creator & Chronicles
Simple solution using only material up through the File chapter.

# ---- Allowed classes (from README) ----
VALID_CLASSES = ["Warrior", "Mage", "Rouge", "Cleric"]

# To keep stats consistent and easy to explain:
# stat = base + growth * level
BASE = {
    "Warrior": {"STR": 12, "MAG": 1, "HP": 90}, # high str, high hp, low magic
    "Mage":    {"STR": 2,  "MAG": 9, "HP": 70}, # low str, high magic, medium hp
    "Rouge":   {"STR": 7,  "MAG": 6, "HP": 60}, # medium, medium, low hp
    "Cleric":  {"STR": 6, "MAG": 10, "HP": 85}, # medium str, high magic, high hp
}
GROWTH = {
    "Warrior": {"STR": 6, "MAG": 1, "HP": 15},
    "Mage":    {"STR": 3, "MAG": 6, "HP": 10},
    "Rouge":   {"STR": 4, "MAG": 3, "HP": 8}, 
    "Cleric":  {"STR": 3, "MAG": 5, "HP": 12},
}
def _gold_for(level):
    # Simple and easy to explain; matches README example at level 1 => 100
    return 100 + 25 * (int(level) - 1)

def create_character(name, character_class):
    """
    Create a new character dictionary with calculated stats. 
    Return: dictionary with keys: name, class, level, strength, magic, health, gold
    """
    if character_class not in VALID_CLASSES:
        return NONE

    level = 1
    stats = calculate_stats(character_class, level) # tuple
    if stats is None:
        return None

    Strength, magic, health = stats
    character = {
        "name": str(name).strip(),
        "class": character_class,
        "level": level,
        "strength": strength,
        "magic": magic,
        "health": health, 
        "gold": _gold_for(level)
    }
    return character
def calculate_stats(character_class, level):
    """
    Calculates base stats based on class and level
    Returns: tuple of (strength, magic, health)
    """
    if character_class not in VALID_CLASSES:
        return None
    try:
        lvl = int(level)
    except ValueError:
        return None
    if lvl < 1:
        return None

    b = BASE[character_class]
    g - GROWTH[character_class]
    strength = b["STR"] + g["STR"] * lvl
    magic    = b["MAG"] + g["MAG"] * lvl
    health   = b["HP"]  + g["HP"]  * lvl
    return (int(strength), int(magic), int(health))

def save_character(character, filename):
    """
    Saves character to text file in specific format
    Returns: True if succesfull, False if error occured (PermissionError)
    Required file format:
    Character Nmae: [name]
    Class: [class]
    Level: [level]
    Strength: [strength]
    Magic: [magic] 
    Health: [health]
    Gold: [gold]
    """
    try:
        with open(filename, "w", encoding="utf-8") as f:
            f.write("Character Name: " + str(character["name"]) + "\n")
            f.write("Class: " + str(character["class"]) + "\n")
            f.write("Level: " + str(character["level"]) + "\n")
            f.write("Strength: " + str(character["strength"]) + "\n")
            f.write("Magic: " + str(character["magic"]) + "\n")
            f.write("Health: " + str(character["health"]) + "\n")
            f.write("Gold: " + str(character["gold") + "\n")
        return True 
    except PermissionError:
        return False

def load_character(filename):
    """ 
    Loads character from text file
    Returns: character dictionary if succesful, None if file not found 
    """
    try: 
        with open(filename, "r", ending="utf-8") as f:
            lines = f.readlines()
    except FileNotFoundError:
        return None

    data = {}
    for line in lines:
        if ":" not in line: 
            continue
        label, value = line.split(":", 1)
        label = label.strip()
        value = value.strip()

        if label == "Character Name":
            data["name"] = value
        elif label == "Class":
            data["class"] = value
        elif label == "Level":
            try:
                data["level"] = int(value)
            except ValueError:
                data["level"] = 1
        elif label == "Strength":
            try:
                data["Strength"] = int(value)
            except ValueError:
                data["Strength"] = 0
        elif label == "Magic":
            try:
                data["magic"] = int(value)
            except ValueError:
                data["magic"] = 0
        elif label == "Health":
            try:
                data["health"] = int(value)
            except ValueError:
                data["health"] = 0
        elif label == "Gold:
            try:
                data["gold"] = int(value)
            except ValueError:
                data["gold"] = 0
    # minimal check that required fields exist
    if "name" in data and "class" in data and "level" in data: 
        return data
    else:
        return None

def display_character(character):
    """
    Prints formatted character sheet 
    Returns: None (prints to console)
    """ 
    Print("=== CHARACTER SHEET ===")
    Print("Name:", character["name"])
    Print("Class:", character["class"])
    Print("Level:", character["level"])
    Print("Strength:", character["strength"])
    Print("Magic:", character["magic"])
    Print("Health:", character["health"])
    Print("Gold:", character["gold"])

def level_up(character)
    """
    Increases character level and recalculates stats 
    Modifies the character dictionary directly 
    Returns: None
    """
    character["level"] = int(character["level"]) + 1 
    s, m , h = calculate_stats(character["class"], character["level"])
    character["strength"] = s
    character["magic"] = m 
    character["health"] = h
    character["gold"] = _gold_for(character["level"])

# Optional small demo
of __name__ == "__main__":
    c = create_character("Aria", "Mage")
    display_character(c)
    save_character(c, "aria.txt")
    c2 = load_character("aria.txt")
    level_up(c2)
    print()
    display_character(c2)

        
        
