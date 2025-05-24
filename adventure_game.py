name = input("Enter your name: ")
print(f"Welcome to the Adventure Game , " , name , "!")
answer = input("You find yourself in a dark forest . Do you wanna go left or right ? (left/right): ").lower()
if answer == "left":
  print("You encounter a wild beast! you have to fight it . ")
  action = input("Do you want to fight or run? (fight/run):").lower()
  if action == "fight":
    print("You bravely fight the beast and win ! you find a treasure chest .")
  elif action == "run":
    print ("You run away safely but you lose the chance to find the treasure .")
  else :
    print("Invalid choice. Please enter 'fight' or 'run'.")
elif answer == "right":
  print("You find a peaceful village . The villagers welcome you warmly and offer you food and shelter for the night.")
  action = input("Do you want to open the treasure chest or to stay in the village? (open/stay):").lower()
  if action == "open":
    print("You open the treasure chest and find gold coins and jewels ! You are now rich and famouse !")
  elif action == "stay":
    print("You enjoy a peaceful night in the village and make new friends .The villagers thank you for your kindness and offer you a place in their community.")
  else :
    print("Invalid choice. Please enter 'fight', 'run', 'open', or 'stay'.")
    exit()
else:
  print("Invalid choice. Please enter 'left' or 'right'.")
  exit()