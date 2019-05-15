import random
print("You can quit the program at any time by inputting 'quit'!\n")
wins = 0
ties = 0
losses = 0
while True:
  choice = input("Rock, paper, or scissors? ").lower()
  if choice == "quit":
    break
  else:
    if choice not in ["rock", "paper", "scissors", "quit"]:
      print("Invalid input!\n")
    else:
      print("You picked:",choice)
      computerChoice = random.choice(["rock", "paper", "scissors"])
      print("The computer picked:",computerChoice)
      if choice == computerChoice:
        print("It's a tie!")
        ties+=1
      elif choice == "rock":
        if computerChoice == "paper":
          print("You lost!")
          losses+=1
        if computerChoice == "scissors":
          print("You win!")
          wins+=1
      elif choice == "paper":
        if computerChoice == "rock":
          print("You win!")
          wins+=1
        if computerChoice == "scissors":
          print("You lose!")
          losses+=1
      elif choice == "scissors":
        if computerChoice == "rock":
          print("You lose!")
          losses+=1
        if computerChoice == "paper":
          print("You win!")
          wins+=1
      print("\nYour record is:",wins,"wins",ties,"ties",losses,"losses\n")
