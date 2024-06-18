#text based slot machine

#global constants, available everywhere, easy to change
MAX_LINES = 3 
MAX_BET = 100
MIN_BET = 1

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

def main():
    balance = deposit() #calling function
    lines = get_number_of_lines() #calling function
    bet = get_bet()
    total_bet = bet * lines
    print(f"You are betting ${bet} on {lines} lines. Total bet is equal to: $ {total_bet}.")

main()