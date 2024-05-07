 # Task 1: Code Correction

# You are provided with a Python script that is supposed to
#  guide a user through an adventure game, but it has some errors. 
# Identify and fix them.


place = input("Choose a place: forest or cave? ")

if place == "forest":
    action = input("climb a tree or cross a river?")
    if action == "climb a tree":
        print("You found a bird's nest!")
    elif action == "cross a river":
        print("You found a boat!")
elif place == "cave":
    print("You find a hidden treasure!")




# Task 2: Setting the Scene

# Based on the corrected code from Task 1, expand the game.
#  If the user chooses "cave", ask them if they want to "light a torch"
# or "proceed in the dark", and provide outcomes for each decision.


place = input("Choose a place: forest or cave? ")

if place == "forest":
    action = input("climb a tree or cross a river?")
    if action == "climb a tree":
        print("You found a bird's nest!")
    elif action == "cross a river":
        print("You found a boat!")
    elif place == "cave":
        print("You find a hidden treasure!")


if place == "cave":
    action = input("would you like a torch, yes or no?")
    if action == "yes":
        print("you see a troll in the distance!")
    elif action == "no":
        print("you can not see beyond the entrace.")

 # Task 3: Default Path

# If the user makes an invalid choice at any point, use the pass statement 
# for now. Later, you can enhance this to provide feedback or a different 
# branch of the story.



place = input("Choose a place: forest or cave? ")

if place == "forest":
    action = input("climb a tree or cross a river?")
    if action == "climb a tree":
        print("You found a bird's nest!")
    elif action == "cross a river":
        print("You found a boat!")
    elif place == "cave":
        print("You find a hidden treasure!")
else:
    pass
    

if place == "cave":
        action = input("would you like a torch, yes or no?")
        if action == "yes":
            print("you see a troll in the distance!")
        elif action == "no":
            print("you can not see beyond the entrace.")

else:
    pass
    




