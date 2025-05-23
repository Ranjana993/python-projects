import random


user_wins = 0
computer_wins= 0 

options = ["rock", "paper", "scissor"]

input_value = input("Do ypu want to play game of rock paper scissor? yes/no:").lower();

if input_value != "yes":
  quit()
print("Welcome to the game rock paper scissors!")


while True:
  user_value = input("Enter a choice or Rock /Paper /Scissor or Q to Quit the game: ").lower()
  if user_value== "q":
    break
  if user_value not in options:
    continue

  random_number = random.randint(0,2);
  # rock = 0 , paper = 1 or scissors = 2
  computer_value = options[random_number]
  print("Computer picked " + computer_value + ".")
  if user_value == "rock" and computer_value == "scissors":
    print("You win!")
    user_wins += 1
    continue
  elif user_value== "paper" and computer_value == "rock":
    print("You win!")
    user_wins+=1
    continue
  else:
    print("You lost!")
    computer_wins+=1

print("You won", user_wins, "times.")
print("Computer won", computer_wins, "times.")
print("Goodbye!")    