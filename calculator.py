try:
    a = int(input("Enter Your first number? "))
    b = int(input("Enter Your first number? "))
    print("Welcome to the world of calculator 🚀")
    print("What you want to do? ")
    print("Press + for addition \nPress - for subtraction \nPress * for multiplication\nPress / for division.")
    print("--------------------------------------------------")
    operation = input("Enter you operation now e.g + , - , * and / ?: ")
    match operation:
        case '+':
          print(f"Your result is: {a+b}")
        case '-':
          print(f"Your result is: {a-b}")
        case '*':
          print(f"Your result is: {a*b}")
        case '/':
          print(f"Your result is: {a/b}")
        case default:
          print("Invalid")  
except Exception as e:
    print(f"Invalid Operation ")