MAX_LINES = 5
MAX_BET = 100
MIN_BET = 10

def deposit():
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

def betting_lines():
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


def get_bet():
    while True:
        bet = input("Enter the amount you wish to bet: £")
        if bet.isdigit():
            bet = int(bet)
            if bet > MIN_BET and bet <= MAX_BET:
                break
            else:
                print(f"Bet must be between £{MIN_BET} and £{MAX_BET}")
        else:
            print("Please enter a valid whole number")
    
    return bet



def main():
    balance = deposit()
    betLines = betting_lines()
    bet = get_bet()
    totalBet = bet * betLines
    print(f"Balance: £{balance}\nBet: £{bet}\nLines: {betLines}")
    print(f"You are betting £{bet} on {betLines} lines. Total bet is £{totalBet}! Good luck!")

main()