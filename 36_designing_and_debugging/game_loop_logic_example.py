# all your functions
def ded():
    print "ded"
    exit(0)
def thing1():
    thing2()
    clock.tick()
def thing2():
    thing3()
    clock.tick()

# all your data

#Start the game
def start():
    # setup vars
    game_clock = Clock()
    game_is_running = true
    while(game_is_running):
        # do thing
        exitted_room = thing()
        if (exitted_room == ROOM.exit):
            clock.tick()
            if (clock.time >= alloted_time):
                ded()