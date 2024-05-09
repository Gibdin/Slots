import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 10

ROWS = 3
COLS = 3

symbol_count = { #How many symbols are in slots
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}

symbol_value = { #Value of each symbol in slots
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}

def check_win(columns, lines, bet, values): #Function to check if user has won their lines, and how much they have won aswell as what lines they have won on
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_check = column[line]
            if symbol != symbol_check:
                break
        else:
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)

    return winnings, winning_lines


def slot_machine(rows, cols, symbols): #Function to create the slot machine
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)
    
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

def print_slots_machine(columns): #Function to print the slot machine
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end = " | ")
            else:
                print(column[row], end = "")
    
        print()


def deposit(): #Function gets the amount the user wants to deposit to play with 
    while True:
        amount = input("Enter the amount you wish to deposit: £")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
               break
            else:
                print("Amount must be greater than 0")
        else:
            print("Please enter a valid whole number")
    
    return amount

def betting_lines(): #Function gets the number of lines the user wishes to bet on
    while True:
        lines = input(f"Enter the number of lines you wish to bet on (1-{MAX_LINES}): ")
        if lines.isdigit():
            lines = int(lines)
            if lines > 0 and lines <= MAX_LINES:
                break
            else:
                print("You can only bet on 1 to", MAX_LINES, "lines")
        else:
            print("Please enter a valid, whole number")
    
    return lines


def get_bet(): #Function gets the amount the users wants to bet.
    while True:
        bet = input("Enter the amount you wish to bet: £")
        if bet.isdigit():
            bet = int(bet)
            if MIN_BET <= bet <= MAX_BET:
                break
            else:
                print(f"Bet must be between £{MIN_BET} and £{MAX_BET}")
        else:
            print("Please enter a valid whole number")
    
    return bet

def spin(balance): #Function to run the slot machine, gets the users bet and lines, then checks if the user has won
    betLines = betting_lines()
    while True:
        bet = get_bet()
        totalBet = bet * betLines
        if totalBet > balance:
            print(f"Insufficient funds. Please enter a lower bet. (balance is {balance})")
        else:
            break

    print(f"Balance: £{balance}\nBet: £{bet}\nLines: {betLines}")
    print(f"You are betting £{bet} on {betLines} lines. Total bet is £{totalBet}! Good luck!")

    slots = slot_machine(ROWS, COLS, symbol_count)
    print_slots_machine(slots)
    winnings, winning_lines = check_win(slots, betLines, bet, symbol_value)
    print(f"You won £{winnings}!")
    print(f"Winning lines:", *winning_lines)
    return winnings - totalBet

    


def main(): #Main function to run the game and get the users balance
    balance = deposit()
    while True:
        print(f"Current Balance is {balance}")
        reply = input("Press enter to spin! (q to quit) ")
        if reply == "q":
            break
        balance += spin(balance)
    
    print(f"Thanks for playing! \nYour final balance is {balance}")


main() 