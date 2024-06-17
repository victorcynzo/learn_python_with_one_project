#text based slot machine

#starting point, collecting user input
def deposit(): #function for collecting user input
    while True: #continually ask until valid, need while loop
        amount = input("What would you like to deposit? $")
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