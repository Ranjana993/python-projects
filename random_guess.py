import random
input_value = input("Do you want to play a random guess number game? yes/no:").lower();
if input_value != "yes":
    quit()
print("Welcome to the random guess number game!")

input_value = input("Please  enter a number of your choice to make guess: ")

if input_value.isdigit():
    input_value = int(input_value)
else:
    print("Please enter a valid number")
    quit();

random_number = random.randint(0 , input_value)
while True:
    guess = input("PLease guess a number to match random number .")
    if guess.isdigit():
        guess = int(guess)
        if guess == random_number:
          print("Congratulations! You guessed the number correctly!")
          break;
        else:
          print("Sorry, you didn't guess the number. Better luck next time!")
    else:
        print("Please enter a valid number")
        continue;