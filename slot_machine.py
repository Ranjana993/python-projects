import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1
ROWS = 3
COLS = 3

symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}

symbol_value = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}

def check_winnings(columns, lines, bet, values):
    winnings = 0
    winnings_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            if column[line] != symbol:
                break
        else:
            winnings += values[symbol] * bet
            winnings_lines.append(line + 1)
    return winnings, winnings_lines

def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, count in symbols.items():
        all_symbols.extend([symbol] * count)

    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)
        columns.append(column)
    return columns

def print_slot_machine(columns):
    print("\n--- SLOT MACHINE ---")
    for row in range(len(columns[0])):
        print(" | ".join(column[row] for column in columns))
    print("---------------------\n")

def deposit():
    while True:
        amount = input("💰 Enter deposit amount: $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                return amount
            print("❗ Amount must be greater than 0.")
        else:
            print("❗ Please enter a valid number.")

def get_number_of_lines():
    while True:
        lines = input(f"🎰 Enter number of lines to bet on (1-{MAX_LINES}): ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                return lines
            print(f"❗ Enter a number between 1 and {MAX_LINES}.")
        else:
            print("❗ Please enter a valid number.")

def get_bet():
    while True:
        amount = input(f"💵 Enter your bet per line (${MIN_BET}-${MAX_BET}): $")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                return amount
            print(f"❗ Bet must be between ${MIN_BET} and ${MAX_BET}.")
        else:
            print("❗ Please enter a valid number.")

def main():
    print("🎉 Welcome to the Python Slot Machine! 🎉\n")
    balance = deposit()

    while True:
        print(f"\nYour current balance is: ${balance}")
        lines = get_number_of_lines()

        while True:
            bet = get_bet()
            total_bet = bet * lines

            if total_bet > balance:
                print(f"❗ Insufficient balance. You have: ${balance}, but your total bet is: ${total_bet}")
            else:
                break

        print(f"\n✅ You are betting ${bet} on {lines} lines. Total bet: ${total_bet}")
        slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
        print_slot_machine(slots)

        winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)
        balance += winnings - total_bet

        print(f"🎉 You won: ${winnings}")
        if winning_lines:
            print("🏆 Winning line(s):", ", ".join(map(str, winning_lines)))
        else:
            print("😢 No winning lines this time.")

        print(f"💼 Your new balance is: ${balance}")

        if balance < MIN_BET:
            print("❌ You don't have enough to continue playing.")
            break

        play_again = input("🔁 Do you want to play again? (y/n): ").lower()
        if play_again != "y":
            print("👋 Thanks for playing! Goodbye!")
            break

if __name__ == "__main__":
    main()
