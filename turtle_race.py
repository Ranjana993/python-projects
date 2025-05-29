import turtle
import time
import random

WIDTH, HEIGHT = 600, 600
COLORS = ["red", "green", "yellow", "black", "pink", "cyan", "orange", "lemon", "brown", "purple", "violet"]

def get_number_of_racers():
    while True:
        racers = input("Enter the number of racers (2 - 10): ").strip()
        if racers.isdigit():
            racers = int(racers)
            if 2 <= racers <= 10:
                return racers
            print("Number must be between 2-10. Try again!")
        else:
            print("Invalid input. Please enter a number.")

def race(racers):
    while True:
        for racer in racers:
            distance = random.randrange(1, 20)
            racer.forward(distance)
            if racer.ycor() >= HEIGHT//2 -30:
                return racer.pencolor()

def create_turtles(colors):
    turtles = []
    spacing = WIDTH / (len(colors) + 1)
    for i, color in enumerate(colors):
        racer = turtle.Turtle()
        racer.color(color)
        racer.shape("turtle")
        racer.penup()
        racer.setpos(-WIDTH//2 + (i + 1) * spacing, -HEIGHT//2 + 20)
        racer.pendown()
        racer.left(90)  # Make turtles face upwards
        turtles.append(racer)
    return turtles

def init_turtle():
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.title("Turtle Racing")
    screen.bgcolor("lightgray") 

def main():
    racers_count = get_number_of_racers()
    init_turtle()
    
    random.shuffle(COLORS)
    colors = COLORS[:racers_count]
    racers = create_turtles(colors)
    
    print("Race starting...")
    winner = race(racers)
    print(f"The winner is the {winner} turtle!")
    turtle.Screen().exitonclick()

if __name__ == "__main__":
    main()