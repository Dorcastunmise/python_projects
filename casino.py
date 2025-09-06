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
    "D": 8,
}

symbol_value = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2,
}


def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line] #if checking row 1 we're looking at the 2nd symbol in each column
            if symbol != symbol_to_check:
                break
        else:  #if we didn't break, we have a win
            winnings += bet * values[symbol] 
            winning_lines.append(line + 1)
    return winnings, winning_lines


def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items(): #i.e A:2, B:4, C:6, D:8
        for _ in range(symbol_count):   # adds each symbol to the list according to its count
            all_symbols.append(symbol)

    columns = []  #empty list 
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:] #[:] creates a copy of the list
        for _ in range(rows):
            value = random.choice(current_symbols) #randomly chooses a symbol from the current list of symbols
            current_symbols.remove(value) #to remove the symbol from the current column after it's been chosen from the column
            column.append(value)

        columns.append(column) #append the column to the list of columns
    return columns

def print_slot_machine(columns): #transposing
    for row in range(len(columns[0])):  #len(columns[0]) = number of rows
        #looping through all of the items in every columns to bring out every column using enumerate to have access to the index and its item
        for i, column in enumerate(columns):    
            if i != len(columns) - 1:   #if it's not the last column using the index
                print(column[row], end=" | ")  #printing each item in the column as row item
            else:
                print(column[row], end="")

        print()

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

def spin(balance):
    lines = lines_no()
    while True:
        bet = get_bet().split('placed')  #['$50.0 ', ''] .split() returns a list
        bet_amount = float(bet[0].strip('$ ').strip())  # extracts numeric part
        total_bet = bet_amount * lines
        if balance < total_bet:
            print(f"Insufficient funds. Your balance is ${balance}, but you are trying to bet ${total_bet}.")
        else: 
            break

    print(f"Your balance is ${balance} and you are betting {bet[0]} on {lines} lines.")
    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet_amount, symbol_value)
    print(f"You won ${winnings}.")
    if winning_lines:
        print(f"You won on ",*winning_lines," lines: ")
    return winnings - total_bet

def main():
    retrieved = deposit().split('deposited')
    balance = float(retrieved[0].strip('$')) if retrieved[0] != '0' else 0
    while True:
        print(f"Current balance is ${balance}")
        answer = input("Press enter to play (q to quit).")
        if answer == 'q':
            break
        balance += spin(balance)

    print(f"You're left with ${balance}")
main()
