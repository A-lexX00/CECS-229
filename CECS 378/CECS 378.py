# -*- coding: utf-8 -*-
"""
Created on Fri Nov 6 07:41:47 2020

@author: alexb
"""

# Where it's at on my copmuter, idk how to route it any other way
file_path = "C:/games/Ultima_5/SAVED.GAM"

# Arrays to store all the values

# You and your NPCs
char_order = {1: "PLAYER", 2: "SHAMINO", 3: "IOLO",
          4: "MARIAH", 5: "GEOFFREY", 6: "JAANA",
          7: "JULIA", 8: "DUPRE", 9: "KATRINA",
          10: "SENTRI", 11: "GWENNO",  12: "JOHNE",
          13: "GORN", 14: "MAXWELL", 15: "TOSHI",
          16: "SADUJ"}

# File location in memory, turns the hex in the file to ints for easier edits
char_offsets = {"PLAYER": int('0x02', 16), "SHAMINO": int('0x22', 16), "IOLO": int('0x42', 16),
            "MARIAH": int('0x62', 16), "GEOFFREY": int('0x82', 16), "JAANA": int('0xA2', 16),
            "JULIA": int('0xC2', 16), "DUPRE": int('0xE2', 16), "KATRINA": int('0x102', 16),
            "SENTRI": int('0x122', 16), "GWENNO": int('0x142', 16), "JOHNE": int('0x162', 16),
            "GORN": int('0x182', 16), "MAXWELL": int('0x1A2', 16), "TOSHI": int('0x1C2', 16),
            "SADUJ": int('0x1E2', 16)}

# Order of the stats you wanna edit
stat_order = {1: "STRENGTH", 2: "INTELLIGENCE", 3: "DEXTERITY",
          4: "HP", 5: "MAXHP", 6: "EXPERIENCE",
          7: "MAGIC"}

# File location in memory, turns the hex in the file to ints for easier edits
stat_offsets = {"STRENGTH": int('0x0C', 16), "INTELLIGENCE": int('0x0E', 16), "DEXTERITY": int('0x0D', 16),
            "HP": int('0x10', 16), "MAXHP": int('0x12', 16), "EXPERIENCE": int('0x14', 16),
            "MAGIC": int('0x0F', 16)}

# What you want your stats to be
stat_max_val = {"STRENGTH": 99, "INTELLIGENCE": 99, "DEXTERITY": 99,
           "HP": 999, "MAXHP": 999, "EXPERIENCE": 9999,
           "MAGIC": 99}

# Items you want us to edit
items_order = {1: "GOLD", 2: "KEYS", 3: "SKULL KEYS",
          4: "GEMS", 5: "BLACK BADGE", 6: "MAGIC CARPET",
          7: "MAGIC AXE"}

# File location in memory, turns the hex in the file to ints for easier edits
item_offsets = {"GOLD": int('0x204', 16), "KEYS": int('0x206', 16), "SKULL KEYS": int('0x20B', 16),
            "GEMS": int('0x207', 16), "BLACK BADGE": int('0x218', 16), "MAGIC CARPET": int('0x20A', 16),
            "MAGIC AXE": int('0x240', 16)}

# What you want your items to be
item_max_val = {"GOLD": 9999, "KEYS": 100, "SKULL KEYS": 100,
           "GEMS": 100, "BLACK BADGE": 1, "MAGIC CARPET": 2,
           "MAGIC AXE": 10}

# Find file and read it in
def read_data():
    with open(file_path, "rb") as save:
        dataBytes = list(bytearray(save.read()))
        save.close()
        return dataBytes
    
# Actually save the data you editted
def write_data(data):
    with open(file_path, "wb") as save:
        save.write(bytearray(data))
        save.close()

# Change your stats
def stat_edit(character, data):
    print("What stat do you wanna change?\n")
    
    print("1.  {}\n2.  {}\n3.  {}\n4.  {}\n5.  {}\n6.  {}\n7.  {}".format(stat_order[1], stat_order[2], stat_order.get(3), stat_order.get(4),
                                                                          stat_order[5], stat_order[6], stat_order[7]))
    # Pick a stat
    choice = int(input())
    
    # The stat you picked
    stat_name = stat_order[choice]
    # The stat of the character
    index = stat_offsets[stat_name] + char_offsets[char_order[character]]
    # Get the biggest stat
    max_val = stat_max_val[stat_name]
    
    # Max out the stat and put it into the game (Game goes by little endidian not big so specify to that)
    counter = 0
    # Make array the length of the max stat
    byte_array = list(bytearray((max_val).to_bytes(2, byteorder="little")))
    if(len(byte_array) == 1):
        byte_array.insert(0, 0)
    # Add to the stat til its done
    for n in byte_array:
        # Edits the hex by adding it one at a time, probs could have done a faster way
        data[index + counter] = n
        # Add by one to slowly increment stat
        counter += 1
    print("{} {} MAXED OUT".format(char_order[character], stat_name))
    
    # Edit other stats?
    choice = input(
        "Would you like to edit another stat? Hit 'Y' to continue or any other letter to leave\n")
    if(choice.lower() == "y"):
        stat_edit(character, data)


def character_select(data):
    print("Select the character you wanna edit")
    # Use format for better looking text
    print("1.  {}\n2.  {}\n3.  {}\n4.  {}\n5.  {}\n6.  {}\n7.  {}\n8.  {}".format(char_order[1], char_order[2], char_order[3], char_order[4],
                                                                                  char_order[5], char_order[6], char_order[7], char_order[8]))
    print("9.  {}\n10. {}\n11. {}\n12. {}\n13. {}\n14. {}\n15. {}\n16. {}".format(char_order[9], char_order[10], char_order[11], char_order[12],
                                                                                  char_order[13], char_order[14], char_order[15], char_order[16]))
    # Select the character you wanna change with your keypad
    choice = int(input())
    
    # Jump to the stat edit function
    stat_edit(choice, data)
    
    # Loop around to edit more characters
    choice = input(
        "Would you like to edit another character? Hit 'Y' to continue or any other letter to leave\n")
    if(choice.lower() == "y"):
        character_select(data)


def edit_character(data):
    character_select(data)
    print("Back to the main\n")
    main_menu(data)  

def item_select(data):
    # Better formating
    print("Which Inventory Item Would You Like to Edit?")
    print("1.  {}\n2.  {}\n3.  {}\n4.  {}\n5.  {}\n6.  {}\n7.  {}".format(items_order[1], items_order[2], items_order[3], items_order[4],
                                                                          items_order[5], items_order[6], items_order[7]))
    # Pick the items you wanna add
    choice = int(input())
            
    # The item from the list
    item_name = items_order[choice]
    
    # Jump to the item value in hex
    index = item_offsets[item_name]
    
    # Max item the teacher wanted
    max_val = item_max_val[item_name]
    
    counter = 0
    # Max out the stat and put it into the game (Game goes by little endidian not big so specify to that)
    bArray = list(bytearray((max_val).to_bytes(2, byteorder="little")))
    # Make array the length of the max stat
    if(len(bArray) == 1):
        bArray.insert(0, 0)
    for n in bArray:
        # Edits the hex by adding it one at a time, probs could have done a faster way
        data[index + counter] = n
        # Add by one to slowly increment stat
        counter += 1
        
    # Tell user they got it
    print("Number of {} MAXED".format(item_name))
    
    # Want more items?
    choice = input(
        "Would you like to Edit Another Amount? Hit 'Y' to continue or any other letter to leave\n")
    if(choice.lower() == "y"):
        item_select(data)


def edit_inventory(data):
    item_select(data)
    print("Back to the main\n")
    main_menu(data)

# User Interface
def main_menu(data):
    print("Ultima 5 Save Editor, Select what you wanna change.\n" + 
          "Enter 1 to edit your character stats\n" +
          "Enter 2 to edit your inventory\n" + 
          "Enter any other number to exit")
    choice = input()
    
    if(choice == "1"):
        edit_character(data)
    elif(choice == "2"):
        edit_inventory(data)
    else:
        write_data(data)
        print("Modified the data, have fun!")


if __name__ == "__main__":
    main_menu(read_data())
