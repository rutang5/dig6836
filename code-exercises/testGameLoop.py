# define a function to handle user input
def handle_input():
    # get user input
    user_input = input("> ")
    # handle user input
    if user_input == "quit":
        # exit the game
        print("Goodbye!")
        exit()
    elif user_input == "n":
        # go north
        print("You go north.")
    elif user_input == "s":
        # go south
        print("You go south.")
    elif user_input == "e":
        # go east
        print("You go east.")
    elif user_input == "w":
        # go west
        print("You go west.")
    else:
        # handle other user input
        print("You said:", user_input)

# define the game loop
def game_loop():
    # print welcome message
    print("Welcome to the game!")
    # start the game loop
    while True:
        # handle user input
        handle_input()

# start the game
game_loop()


