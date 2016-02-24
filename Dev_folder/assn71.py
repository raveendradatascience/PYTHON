# *************************************************************************************************
#
#7.1 Write a program that prompts for a file name, then opens that file and reads through the file,
#and print the contents of the file in upper case. Use the file words.txt to produce the output below.
# You can download the sample data at http://www.pythonlearn.com/code/words.txt
#
#*****************************************************************************************************

name = raw_input('Enter file:') # prompts user to give file name
fh = open(name) # gets opens file and store fh as handle
for line in fh: # looping for every line
    line = line.rstrip() # to strip \n for every new line.
    upper_line = line.upper() # converting every line as upper
    print upper_line # printing final output.
