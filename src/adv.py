from room import Room
from player import Player
from item import Item
import random
# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}
# Items
item = {
    'Purse': Item("\nCoin Purse", "A leather sack with several valuable coin pieces."),
    'Sword': Item("Sword", "\nA well-worn sword, looks like its remained from a previous owner of this cave who didn't make it out."),
    'Potion': Item("Potion", "\nA potion vial containing a strange color liquid. If you drink it side effects may vary."),
    'Book': Item("Book", "A worn down book whose title reads 'how to find the treasure without dying'."),
    'Torch': Item("Torch", "A burnt out torch. Could be used again if re-lightened.")
}
# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']


#
# Main
#

# Make a new player object that is currently in the 'outside' room.
player = Player("Andrew", room['outside'])

game_running = True

# Write a loop that:
# * Prints the current room name
       
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

while game_running: 
    print("You currently stand in the %s, \n%s" % (player.current_room.name, player.current_room.description))
    # print(player.current_room)
    # room[player.current_room].loot = []
    loot_table = random.sample(list(item), 2)
    player.current_room.add_item(loot_table)
    print(f'A glint of light catches your eye, it looks like a {loot_table} lies inside this room.')

    player_input = input("Which direction shall you proceed? [n]:North, [s]:South, [e]:East, or [w]:West?\n To pickup an item select [get] [item name] , to drop an item select 'drop': item-name.").split(' ')
    if str(player_input[0]).lower() == 'q':
        game_running = False
        print("You have exited the game!")
    elif str(player_input[0]).lower() == 'n':
        if player.current_room.n_to:
            player.current_room = player.current_room.n_to
        else:
            print("That Path isn't a valid one, please choose a new path.")
    elif str(player_input[0]).lower() == 's':
        if player.current_room.s_to:
            player.current_room = player.current_room.s_to
        else:
            print("That Path isn't a valid one, please choose a new path.")
    elif str(player_input[0]).lower() == 'w':
        if player.current_room.w_to:
            player.current_room = player.current_room.w_to
        else:
            print("That Path isn't a valid one, please choose a new path.")
    elif str(player_input[0]).lower() == 'e':
        if player.current_room.e_to:
            player.current_room = player.current_room.e_to
        else:
            print("That Path isn't a valid one, please choose a new path.")
    elif str(player_input[0]).lower() == 'get':
    #  and str(player_input[1]).lower().split() == loot_table[0]:
            player.add_item(loot_table[0])
            print(loot_table)
            print(f"You've picked up the {loot_table[0]}! It is now stored in you inventory.")
            print(f"Current Inventory: {player.inventory}")
    elif str(player_input[0]).lower().split() == 'drop':
    # and str(player_input[1]).lower().split() == loot_table[0]:
            player.drop_item(player.inventory)
            print(loot_table)
            print(f"You've dropped the item!")
            print(f"Current Inventory: {player.inventory}")
    # elif str(player_input[0]) == 'help':
    #     print('no help provided, good luck budday...')
    
        




