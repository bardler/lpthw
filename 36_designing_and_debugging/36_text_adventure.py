#lpthw exercise 36 text adventure
#import libraries
from sys import exit

#global inventory list
inventory = []

#all room functions accessible in house, acts a hub
def house():
    choice = raw_input("What room would you like to go? ").lower()
    if choice == "living room":
        living_room()

    elif choice == "kitchen":
        kitchen()

    elif choice == "garage" and "garage key" in inventory:
        print "You unlocked the Garage with the Garage Key!"
        garage()

    elif choice == "garage" and "garage key" not in inventory:
        garage_locked()

    elif choice == "exit game":
        exit(0)

    else:
        print "Not a valid option"
        print "options are [living room] [kitchen] [garage] [exit game]"
        house()

#rooms
def crate():
    print "You are locked in the crate"
    explored_room = False
    get_item = False

    while True:
        choice = user_control()

        if choice == "explore room":
            print "You see a great big world outside of this crate."
            print "Just outside the crate is a Fanny Pack [item]"
            explored_room = True

        elif choice == "get item" and explored_room:
            print "You picked up the Fanny Pack, and dig around inside."
            print "You find a lot of bird seed, but it doesn't taste very good."
            print "Bob the Parrot flies over to cage and offers to let you out if you give him the bird seed."
            get_item = True

        elif choice == "use item" and get_item:
            print "You give the Fanny Pack to Bob"
            print "He lets you out of the crate!"
            house()

        elif choice == "exit room":
            print "You didn't think it was that easy?"

        else:
            print "Not Valid"


def living_room():
    print "Welcome to the Living Room"
    explored_room = False

    while True:
        choice = user_control()

        if choice == "use item":
            print "There is nothing to use items on in here"

        elif choice == "explore room":
            print "You look around the room, and notice a key on the coffee table"
            explored_room = True

        elif choice == "get item" and explored_room:
            print "You picked up the Garage Key"
            inventory.append("garage key")

        elif choice == "get item" and not explored_room:
            print "You have not looked around the room yet"

        else:
            print
            "not valid"

def kitchen():
    print "Welcome to the Kitchen"
    explored_room = False

    while True:
        choice = user_control()

        if choice == "use item" and "ladder" in inventory:
            print "You use the ladder and won!"
            exit(0)

        elif choice == "use item" and "ladder" not in inventory:
            print "You do not have the correct item"

        elif choice == "explore room":
            print "The treats are on the counter just out of reach."
            explored_room = True

        elif choice == "get item" and explored_room:
            print "There is no item in the Kitchen"

        else:
            print
            "not valid"


def garage():
    print "Welcome to the Garage"
    explored_room = False

    while True:
        choice = user_control()

        if choice == "use item":
            print "There is nothing to use items on in here"

        elif choice == "explore room":
            print "You look around the room, and notice there is a nice ladder in the corner"
            explored_room = True

        elif choice == "get item" and explored_room:
            print "You picked up the ladder"
            inventory.append("ladder")

        elif choice == "get item" and not explored_room:
            print "You have not looked around the room yet"

        else:
            print
            "not valid"

def garage_locked():
    print "The Garage is locked"
    print "You need a key"
    house()

#game loop and functions
def dead():
    print "You Lost"
    exit(0)

def user_control():
    #Explore Room, Exit Room, Get Item, Use Item,
    print "What would you like to do?"
    choice = raw_input("> ").lower()
    if choice == "explore room":
        return choice

    elif choice ==  "get item":
        return choice

    elif choice == "use item":
        return choice

    elif choice == "exit room":
        house()

    elif choice == "exit game":
        exit(0)

    else:
        print "The options are [explore room] [exit room] [get item] [use item] [exit game]"


def start():
    print "Welcome to The Great Puppy Adventure"
    print "You are curious puppy named: "
    puppy_name = raw_input("> ")
    print "%s is hungry, there are some treats somewhere in the house" % puppy_name
    print "You just have to find a way to get them..."

    game_is_running = True
    while game_is_running:
        crate()

start()