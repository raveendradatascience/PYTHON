#**********************************************************************************************
# 4.6 Write a program to prompt the user for hours and rate per hour using raw_input           #
# to compute gross pay. Award time-and-a-half for the hourly rate for all hours                #
# worked above 40 hours. Put the logic to do the computation of time-and-a-half                #
# in a function called computepay() and use the function to do the computation.                #
# The function should return a value. Use 45 hours and a rate of 10.50 per hour                #
# to test the program (the pay should be 498.75). You should use raw_input to read             #
# a string and float() to convert the string to a number. Do not worry about error             #
# checking the user input unless you want to - you can assume the user types numbers properly. #
# Do not name your variable sum or use the sum() function.                                     #
# *********************************************************************************************


inp=raw_input("Enter Hours:") # user enters hours as text
hours=int(inp) # converting string as integer
inp=raw_input("Enter rate per hour:") # prompts user to enter rate per hour
rate=float(inp) # converting string as float
def computepay(hours,rate) : # defining computepay method
    rate_exhr=rate*1.5
    exthr=hours-40
    expay=exthr*rate_exhr
    nrmlpay=40*rate
    pay=expay+nrmlpay
    return pay
if hours>40 : # checking the condition hours worked
    print computepay(hours,rate)
else :
    pay=hours*rate
    print pay
