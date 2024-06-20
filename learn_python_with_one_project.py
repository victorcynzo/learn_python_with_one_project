#text based slot machine, 3x3 reel slotmachine, 3 in a row

import random #generate slotmachine values randomly

#global constants, available everywhere, easy to change
MAX_LINES = 3 #betting on lines is top to bottom
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

#how many symbols in each reel, lower letter higher number (times winning)
symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8,
}

#multiplier for winnings
symbol_value = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2,
}

def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines): #iterate through lines/row, index 0 - 2 aka line 1 - 3
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line] # = symbol at current row in column
            if symbol != symbol_to_check:
                break #not equal to previous then break out of loop
        else: #runs if break does not run
            winnings += values[symbol] * bet
            winning_lines.append(line +1)
    return winnings, winning_lines


#generate outcome slotmachine
def get_slot_machine_spin(rows, cols, symbols):
    #create list with all possible values and randomly choose 3, remove from list and choose again, not most efficient algorithm
    all_symbols = []
    for symbol, symbol_count in symbols.items(): #can do because dict, .items gives both key and value
        for _ in range(symbol_count): # _ is anonymous variable, doesn't care about count/variable
            all_symbols.append(symbol) #adding a twice to all_symbols list
        
    #what symbol in what column
    columns = [] #nested list, each nested list is value in column, storing columns
    #generate random value inside column, how many rows we have
    for _ in range(cols): #for every column, so three times
        column = []
        current_symbols = all_symbols[:] #copy of list
        for _ in range(rows): #loop through number of values
            value = random.choice(current_symbols) #use copy of list, remove value afterwards to not be able to pick 4 A's
            current_symbols.remove(value) #remove from copied list, can't pick it again
            column.append(value) #add value to column
        
        columns.append(column)
    
    return columns

def print_slot_machine(columns): #print out slot machine, not easy format to print, laid out as rows, need to flip to print
    #transposing matrix
    #loop through every single row
    for row in range(len(columns[0])): #length of columns, crashes if there's no columns, assume we always have one
        for i, column in enumerate(columns): #looping through all columns, only print row we're on
            #enumerate gives index and loop through
            if i != len(columns) - 1: #is max index to access index in columns list, max index is len-2 (3 items, index is 2)
                print(column[row], end=" | ") #pipe operator, keeps print on same line instead of next line
            else:
                print(column[row], end="")
        print() #brings down to next line after one row, not everything on one line

#starting point, collecting user input
def deposit(): #function for collecting user input
    while True: #continually ask until valid, need while loop
        amount = input("What would you like to deposit? $ ")
        #check if amount is number
        if amount.isdigit(): #works with whole positive numbers
            amount = int(amount) #convert string to integer
            if amount > 0:
                break #out of while loop, when amount bigger than 0
            else:
                print("Amount must be greater than 0.") #when amount is smaller than 0
        else:
            print ("Please enter a number") #when text is entered
    return amount #return amount after function is called

#amount to bet on each line
def get_bet():
    while True:
        amount = input("What would you like to bet on each line? $ ")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Amount must be between {MIN_BET} and {MAX_BET}") #way to incorporate valuable in string
        else:
            print("Please enter a number.")
    return amount

#collect bet from the user
def get_number_of_lines():
    while True:
        lines = input("Enter the number of lines to bet on (between 1 and " + str(MAX_LINES) + ")? ") #add variable to string input
        if lines.isdigit(): #check if it's anumber
            lines = int(lines) #convert to integer
            if 1 <= lines <= MAX_LINES: #number of lines between 1 and 3
                break
            else:
                print("Amount must be between 1 and " + str(MAX_LINES) + "")
        else:
            print("Please enter a number")
    return lines #return after function is 'completed'


def spin(balance):
    lines = get_number_of_lines() #calling function
    while True:
        bet = get_bet()
        total_bet = bet * lines

        if total_bet > balance:
            print(f"You do not have enough balance to bet that amount, your current balance is ${balance}.")
        else:
            break
    print(f"You are betting ${bet} on {lines} lines. Total bet is equal to: $ {total_bet}.")

    slots = get_slot_machine_spin(ROWS, COLS, symbol_count) 
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)
    if winnings > 0:
        print(f"You won ${winnings}!")
    if len(winning_lines) > 0:
        print(f"You won on lines: ", *winning_lines) # *unpacks list and passes both values
    else:
        print("You have not won on any lines.")
    return winnings - total_bet

def main():
    balance = deposit() #calling function
    while True:
        print(f"Current balance is : ${balance}.")
        answer = input("Press enter to play (q to quit).")
        if answer == "q":
            break
        balance += spin(balance)
    
    print(f"You left with ${balance}")

main()