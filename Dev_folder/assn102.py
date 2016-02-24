# ******************************************************************************#
# 10.2 Write a program to read through the mbox-short.txt and figure out the    #
# distribution by hour of the day for each of the messages. You can pull the    #
# hour out from the 'From ' line by finding the time and then splitting the     #
# string a second time using a colon.                                           #
# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008                      #
# Once you have accumulated the counts for each hour, print out the counts,     #
# sorted by hour as shown below.                                                #
#*******************************************************************************#

fname = raw_input("Enter file name: ") # prompts user to enter filename string
fh = open(fname)  # opens and reads the file name.
counts=dict() # invoking a dictionary
lst=list() # invoking a list
for line in fh: # looping lines
    nospln=line.rstrip() # stripping \n character at end of line.
    if (nospln.startswith("From ")) : # finding required word
        words=nospln.split() # splitting words
        for word in words : # looping the words
            tmp=word.split(':') # splitting words with delimiter ':'
            for t in tmp :
                lst.append(t) # append s list
    if lst[5] in counts : # finding required word in dictionary
        counts[lst[5]]=counts[lst[5]]+1 # increasing dictionary counter
    else :
        counts[lst[5]]=1 #
lt=counts.items()
lt=lt.sort()# soritng of tuples
print lt
