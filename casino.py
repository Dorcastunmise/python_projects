MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1


def deposit():
    while True:
        amount = input("Enter amount to deposit (or 'q' to quit) $")
        if amount == 'q':
            break
        if amount.isdigit():
            amount = float(amount)
            if amount > 0:
                break
            else:
                print("Invalid amount. Please enter a positive number.")
                continue
        else:
            print("Invalid input. Please enter a number.")
    return f"${amount} deposited" if amount != 'q' else 0

def lines_no():
    while True:
        lines = input("Enter the number of lines to bet on (1-" + str(MAX_LINES) + ")? ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print(f"Invalid input. Please enter a number between 1 and {MAX_LINES}.")
                continue
        else:
            print("Invalid input. Please enter a number.")
    return lines

def get_bet():
    while True:
        amount = input("What would you like to bet on each line? $")
        if amount.isdigit():
            amount = float(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Invalid amount. Please enter a number between ${MIN_BET} and ${MAX_BET}.")
                continue
        else:
            print("Invalid input. Please enter a number.")
    return f"${amount} placed"

def main():
    retrieved = deposit().split('deposited')
    balance = float(retrieved[0].strip('$')) if retrieved[0] != '0' else 0
    lines = lines_no()
    bet = get_bet().split('placed')
    print(f"Your balance is ${balance} and you are betting {bet[0]} on {lines} lines.")

main()
