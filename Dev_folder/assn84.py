#*********************************************************************************#
# 8.4 Open the file romeo.txt and read it line by line. For each line, split the  #
# line into a list of words using the split() method. The program should build a  #
# list of words. For each word on each line check to see if the word is already   #
# in the list and if not append it to the list. When the program completes, sort  #
# and print the resulting words in alphabetical order.                            #
# You can download the sample data at http://www.pythonlearn.com/code/romeo.txt   #
#*********************************************************************************#
fname = raw_input("Enter file name: ") # user enters the file name.
fh = open(fname) # opens and reads the file name.
lst = list()# invoking list
for line in fh:  # reading each line
    nospln=line.rstrip() # stripping of \n character at end of line
    words=line.split() # splitting the words
    for word in words : #
        if word not in lst : lst.append(word) # checking avaialable word list.
lst.sort() # sorting of list
print lst # printing final list
