#text based slot machine

#global constants, available everywhere, easy to change
MAX_LINES = 3 

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

#collect bet from the user
def get_number_of_lines():
    while True:
        lines = input("Enter the number of lines to bet on (1-" + str(MAX_LINES) + ")?") #add variable to string input
        if lines.isdigit(): #check if it's anumber
            lines = int(lines) #convert to lines
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Amount must be between (1-" + str(MAX_LINES) + ")")
        else:
            print("Please enter a number")
    return lines

def main():
    balance = deposit() #calling function
    lines = get_number_of_lines()
    print(balance, lines)

main()