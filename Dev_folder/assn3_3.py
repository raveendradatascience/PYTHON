#********************************************************************************************
#3.3 Write a program to prompt for a score between 0.0 and 1.0. If the score is out of range,
#print an error. If the score is between 0.0 and 1.0, print a grade using the following table:
#
#********************************************************************************************

inp=float(raw_input("Enter score between 0.0 and 1.0 : ")) # promps for user input.
if inp>= 0.0 : # checking input
    if inp<=1.0 : # checking agaian for another condition
        if inp>=0.9 : print 'A' # checking and printing
        elif inp>=0.8 : print 'B'# checking and printing
        elif inp>=0.7 : print 'C'# checking and printing
        elif inp>=0.6 : print 'D'# checking and printing
        else : print 'F'# checking and printing
    else : print "Entered score is Greater than 1.0,enter between 0.0 and 1.0"
else : print "Entered Score is less than Zero enter between 0.0 and 1.0"
