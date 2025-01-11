print("Welcome to the Gaming Lobby\n")

gamingLobby = {}


# Make this function modify the current level that a player is
# Remember, only positive level changes (>0) because nobody goes down a level
def modifyLevel(playerName, levelChange):
    print(f"Processing modifylevel for {playerName} and level {levelChange}.")

    # Check if the player is in the gaming lobby first of all


    # Then check if the level change is positive


    # If both of these conditions are true, then you can change the level


    # Otherwise, print that either the player isn't in the lobby
    # Or a message stating that 'level change must be positive'

# Make this function add a player to the gaming lobby
def addPlayer(playerName, playerLevel):
    print(f"Processing addPlayer for {playerName} and level {playerLevel}.")

    # Check if the player is already in the lobby
    # If they are, don't add the player


    # Then check if the playerLevel is above 0 (>0)
    # Player levels can't be negative (it just doesn't make sense)


    # If the player isn't in the lobby, and the level is valid,
    # add the player to the dictionary with along with their starting level

# Make this function remove a player to the gaming lobby
def removePlayer(playerName):
    print(f"Processing removePlayer for {playerName}.")

    # Check if the player is in the lobby


    # If so, remove the player from the lobby


    # Otherwise, print that the player isn't in the lobby

# THIS IS AN OPTIONAL FUNCTION (YOU DO NOT NEED TO INCLUDE IT)
# If you don't include this function, comment out the header
# Also, remove the section of code in the main code that mentions 'leaderboard'
def leaderboard():
    print(f"Processing leaderboard.")

    # To print the leaderboard, you will need to do extra research
    # On how to sort a dictionary based on the values
    # Or you can prove me wrong and come up with a solution with what we've       learned


# Main code
while True:
    print("\n1. Modify a player's level.")
    print("2. Add a new player to the gaming lobby.")
    print("3. Remove a player from the gaming lobby.")

    # You can delete choice 4 if you aren't doing the leaderboard function
    print("4. View the leaderboard.")
    print("5. Stop.")

    choice = input("Enter your choice (1/2/3/4/5): ")

    # If choice is 1, ask for the player name and the level change
    # Then call the modifyLevel function
    if choice == "1":
        name = input("Please enter the player's name: ")
        level = input(f"Please enter {name}'s level: ")
        modifyLevel(name, level)

    # If choice is 2, ask for the player name and the player level
    # Then call the addPlayer function
    if choice == "2":
        name = input("Please enter the player's name: ")
        level = input(f"Please enter {name}'s level: ")
        addPlayer(name, level)


    # If choice is 3, ask for the player name
    # Then call the removePlayer function
    if choice == "3":
        name = input("Please enter the player's name: ")
        removePlayer(name)

    # If choice is 4, call the leaderboard function
    if choice == "4":
        leaderboard()

    # If choice is 5, break from the while True loop
    if choice == "5":
        break

    # Otherwise, the user choice was invalid. Simply state choice was invalid


