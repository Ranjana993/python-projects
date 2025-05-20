playing = input("Do you want to play a quiz game? (yes/no): ").lower()
if playing != "yes":
    quit()
print("Welcome to the quiz game!")
print("You will be asked 5 questions.")
print("For each question, type the letter of the correct answer. Let's start!")

score = 0
questions = [
    {
        "question": "What is the capital of France?",
        "options": ["a) Paris", "b) London", "c) Berlin", "d) Madrid"],
        "answer": "a"
    },
    {
        "question": "What is the largest planet in our solar system?",
        "options": ["a) Earth", "b) Jupiter", "c) Saturn", "d) Mars"],
        "answer": "b"
    },
    {
        "question": "Who wrote 'Romeo and Juliet'?",
        "options": ["a) Mark Twain", "b) Charles Dickens", "c) William Shakespeare", "d) Jane Austen"],
        "answer": "c"
    },
    {
        "question": "What is the chemical symbol for gold?",
        "options": ["a) Au", "b) Ag", "c) Pb", "d) Fe"],
        "answer": "a"
    },
    {
        "question": "What is the speed of light?",
        "options": ["a) 300,000 km/s", "b) 150,000 km/s", "c) 1,000 km/s", "d) 3,000 km/s"],
        "answer": "a"
    }
]


for i, q in enumerate(questions):
    print(f"\nQuestion {i + 1}: {q['question']}")
    for option in q['options']:
        print(option)
    answer = input("Your answer: ").lower()
    if answer == q['answer']:
        print("Correct!")
        score += 1
    else:
        print(f"Wrong! The correct answer is {q['answer']}.")


print(f"\nYour final score is {score} out of {len(questions)}.")
if score == len(questions):
    print("Congratulations! You got all the answers right!")
elif score >= len(questions) / 2:
    print("Good job! You passed the quiz.")
else:
    print("Better luck next time! You can do it!")
print("Thank you for playing the quiz game!")