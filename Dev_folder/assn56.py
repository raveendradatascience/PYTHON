#*************************************************************************************
#5.6 Write a program that repeatedly prompts a user for integer numbers until          #
#the user enters 'done'. Once 'done' is entered, print out the largest and smallest    #
# of the numbers. If the user enters anything other than a valid number catch it       #
#with a try/except and put out an appropriate message and ignore the number.           #
#Enter the numbers from the book for problem 5.1 and Match the desired output as shown.#
#**************************************************************************************#
largest=None # initialised largest as python defiend constant
smallest=None# initialised largest as python defiend constant
while True :# usage of True while
    inp=raw_input("Enter a number :")# prompts for enter a number
    if inp == "done" : break  # checking input received
    try : # usage exceptional handling
        inp= int(inp) # converting string as integer
        if largest is None : largest=inp # checking of initialised value has changed or not.
        elif inp>largest : largest=inp # checking if initialised value has changed then to be assigned with input
        if smallest is None : # checking of initialised value has changed or not.
            smallest=inp # assining input to smallest
        elif inp<smallest : smallest=inp
    except : # exceptional handling
        print "Invalid input" # prompting as invalid input.
        continue # if it is invalid continues to top of while loop
print "Maximum is", largest
print "Minimum is", smallest
