# Spooky Escape Room

## Objective
Design a simple, text-based escape room game using variables, loops, and conditional logic. Implement "lock and key" type puzzles where an item obtained from one room is necessary to unlock another room and progress through the game. The game should include at least three rooms and a basic inventory system.

## Instructions
1. Create a Python program that simulates a spooky escape room game.
2. The game should start by providing a spooky introduction and setting the scene for the players.
3. Implement a function for each room in the game, where each function represents a different room.
4. Each room function should display a description of the room and provide options for the player to interact with the environment or objects in the room.
5. Use variables to keep track of the player's progress, current room, and the items they have collected in their inventory.
6. Use loops and conditional statements to guide the player through the game and handle different scenarios based on their choices.
7. Create "lock and key" puzzles where the player needs to find and use specific items to unlock doors or access new areas.
8. Include at least three rooms with unique puzzles and challenges. Make sure to design a logical progression, where the player needs to solve puzzles in a specific order to advance.
9. Implement a basic inventory system using lists or dictionaries to keep track of the items the player has collected.
10. Once the player successfully escapes the final room, display a winning message and end the game.

### Extra Challenges (optional)
- Add a timer or limited number of moves to increase the challenge.
- Implement additional puzzle types, such as riddles or math problems.
- Enhance the game with ASCII art, sound effects, or spooky ambiance.

**Note:** Feel free to add additional features to make it more engaging and challenging. Good luck, and have fun with your Spooky Escape Room game!

# Stuck? Need Help Getting Started? 
Try to develop a framework on your own first, but if you need a basic game loop structure to get you started, here is some Python code you can tinker with.

  ```
  def introduction():
      print("Welcome to the Spooky Escape Room!")
      print("You find yourself trapped in a mysterious room...")
      # Add more spooky details and setup here
  
  def room1():
      print("Room 1")
      # Add room description and options for interaction
  
  def room2():
      print("Room 2")
      # Add room description and options for interaction
  
  def room3():
      print("Room 3")
      # Add room description and options for interaction
  
  inventory = []
  
  def play_game():
    
    introduction()
    room1()
  
    while True:
        choice = input("Enter your choice: ")
  
        if choice == "1":
            room2()
        elif choice == "2":
            room3()
        elif choice == "3":
            # Add code for handling other options/interactions
            pass
        else:
            print("Invalid choice. Try again.")
  
  play_game()
```
