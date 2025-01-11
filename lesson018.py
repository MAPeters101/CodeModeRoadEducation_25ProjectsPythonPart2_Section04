videoGameScores = {"sam":9, "susan":88, "johnny":1000, "trevor":14, "annie":987}

print(videoGameScores)

choice = int(input("Do you want to: \n(1) Change the score of a player\n(2) Delete a player \n(3) Add a player\n"))

while choice > 3 or choice < 1:
    print("Invalid")
    choice = int(input(
        "Do you want to: \n(1) Change the score of a player\n(2) Delete a player \n(3) Add a player\n"))


