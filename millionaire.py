questions = [
    ["Which element has the chemical symbol 'O'?", "Gold", "Oxygen", "Osmium", "Iron", 2],
    ["Who is known as the 'Father of Computers'?", "Charles Babbage", "Albert Einstein", "Thomas Edison", "Nikola Tesla", 1],
    ["In which year did World War II end?", "1943", "1945", "1950", "1939", 2],
    ["What is the currency of Japan?", "Yuan", "Won", "Yen", "Dollar", 3],
    ["Which sport is played at Wimbledon?", "Tennis", "Cricket", "Soccer", "Golf", 1],
    ["How many continents are there?", "5", "6", "7", "8", 3],
    ["Who discovered gravity?", "Isaac Newton", "Galileo", "Einstein", "Copernicus", 1],
    ["Which animal is the national symbol of Australia?", "Kangaroo", "Koala", "Emu", "Lion", 1],
    ["What is the hardest natural substance on Earth?", "Gold", "Iron", "Diamond", "Platinum", 3],
    ["Which language has the most native speakers?", "English", "Hindi", "Spanish", "Mandarin", 4],
    ["Who is the author of 'Harry Potter'?", "J.R.R. Tolkien", "J.K. Rowling", "George R.R. Martin", "Stephen King", 2],
    ["Which planet is closest to the Sun?", "Venus", "Earth", "Mars", "Mercury", 4],
    ["What is the largest organ in the human body?", "Heart", "Liver", "Skin", "Brain", 3],
    ["Which country is home to the kangaroo?", "South Africa", "Brazil", "Australia", "New Zealand", 3],
    ["How many sides does a hexagon have?", "5", "6", "7", "8", 2],
    ["Which famous scientist developed the theory of relativity?", "Newton", "Darwin", "Einstein", "Tesla", 3],
    ["What is the main ingredient in guacamole?", "Tomato", "Avocado", "Onion", "Pepper", 2],
    ["Which gas do plants absorb from the atmosphere?", "Oxygen", "Carbon Dioxide", "Nitrogen", "Hydrogen", 2],
    ["Which instrument has 88 keys?", "Guitar", "Violin", "Piano", "Flute", 3],
    ["Who was the first person to step on the Moon?", "Buzz Aldrin", "Neil Armstrong", "Yuri Gagarin", "Michael Collins", 2]
]

prizes = [100, 150, 200, 250, 300, 350, 400, 450, 500, 550,600, 650, 700, 750, 800, 850, 900, 950, 1000, 1050]

total_prize = 0
current_question = 0

user = input("Hey do you want to be a millionaire? If yes then press 'yes' otherwise press 'no' (yes/no): ").lower()

if user != "yes":
    print("Maybe next time!")
    quit()

print("\nGreat! Let's begin the game. For each correct answer, you'll win money!\n")

while current_question < len(questions):
    question = questions[current_question]
    print(f"\nQuestion for ₹{prizes[current_question]}:")
    print(question[0])
    print("\nOptions:")
    print(f"a. {question[1]}")
    print(f"b. {question[2]}")
    print(f"c. {question[3]}")
    print(f"d. {question[4]}")
    
    user_ans = input("\nEnter your answer (1-4): ")
    
    # Validate input
    if user_ans not in ['1', '2', '3', '4']:
        print("Invalid input! Please enter 1, 2, 3, or 4.")
        continue
    
    if int(user_ans) == question[5]:
        total_prize = prizes[current_question]
        print(f"\n✅ Correct! You've won ₹{total_prize} so far!")
        current_question += 1
        
        if current_question < len(questions):
            print("\nMoving to the next question...")
        else:
            print("\n🎉 Congratulations! You answered all questions correctly!")
            print(f"🏆 Total prize money won: ₹{total_prize}!")
    else:
        correct_option = question[5]
        print(f"\n❌ Incorrect! The correct answer was option {correct_option}: {question[correct_option]}")
        print(f"\nGame Over! You won ₹{total_prize}!")
        break

print("\nThanks for playing!")