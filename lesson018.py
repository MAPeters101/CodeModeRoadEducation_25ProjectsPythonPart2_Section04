videoGameScores = {"sam":9, "susan":88, "johnny":1000, "trevor":14, "annie":987}

print(videoGameScores)

choice = int(input("Do you want to: \n(1) Change the score of a player\n(2) Delete a player \n(3) Add a player\n"))

while choice > 3 or choice < 1:
    print("Invalid")
    choice = int(input(
        "Do you want to: \n(1) Change the score of a player\n(2) Delete a player \n(3) Add a player\n"))

if choice == 1:
    changePlayer = input("Which player's score do you want to change: ")
    if changePlayer in videoGameScores:
        changeScore = int(input(f"What is {changePlayer}'s new score: "))
        videoGameScores[changePlayer] = changeScore
    else:
        print("Invalid")

if choice == 2:
    remPlayer = input("Which player do you want to remove: ")
    if remPlayer in videoGameScores:
        del videoGameScores[remPlayer]
    else:
        print("Invalid")

if choice == 3:
    newPlayer = input("What's the name of the new player: ")
    newScore = int(input(f"What is {newPlayer}'s score: "))
    videoGameScores[newPlayer] = newScore

print(videoGameScores)

