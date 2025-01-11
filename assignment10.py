print("Welcome to the Gaming Lobby\n")

gamingLobby = {}

def modifyLevel(playerName, levelChange):
    if playerName in gamingLobby:
        if level > 0:
            gamingLobby[playerName] += levelChange
        else:
            print("The level change must be positive.")
    else:
        print(f"{playerName} is not in the lobby.")

def addPlayer(playerName, playerLevel):
    if playerName in gamingLobby:
        print(f"{playerName} is already in the lobby.")
    else:
        if playerLevel > 0:
            gamingLobby[playerName] = playerLevel
        else:
            print("The player's level must be positive.")

def removePlayer(playerName):
    if playerName in gamingLobby:
        del gamingLobby[playerName]
    else:
        print(f"{playerName} isn't in the lobby.")

def leaderboard():
    leaders = sorted(gamingLobby.items(), key=lambda x: x[1], reverse=True)
    print(leaders)

while True:
    print("\n1. Modify a player's level.")
    print("2. Add a new player to the gaming lobby.")
    print("3. Remove a player from the gaming lobby.")
    print("4. View the leaderboard.")
    print("5. Stop.")

    choice = input("Enter your choice (1/2/3/4/5): ")
    if choice == "1":
        name = input("Please enter the player's name: ")
        level = int(input(f"Please enter {name}'s level change: "))
        modifyLevel(name, level)
    elif choice == "2":
        name = input("Please enter the player's name: ")
        level = int(input(f"Please enter {name}'s level: "))
        addPlayer(name, level)
    elif choice == "3":
        name = input("Please enter the player's name: ")
        removePlayer(name)
    elif choice == "4":
        leaderboard()
    elif choice == "5":
        break
    else:
        print("Invalid entry.")

