def deposit():
    while True:
        amount = input("Enter the amount you wish to deposit: $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0")
        else:
            print("Please enter a whole number")
    return amount