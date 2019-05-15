from random import randint
dice = input("What kind of dice are you playing with?: ")
amountOfDice, amountOfSides = dice.split("d")
rollList = []
for x in range(int(amountOfDice)):
    roll = randint(1, int(amountOfSides))
    rollList.append(roll)
print(sum(rollList), "\nInvidual rolls:", rollList)
