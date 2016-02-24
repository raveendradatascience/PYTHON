#********************************************************************************#
# 9.4 Write a program to read through the mbox-short.txt and figure out who has  #
# the sent the greatest number of mail messages. The program looks for 'From '   #
# lines and takes the second word of those lines as the person who sent the mail.#
# The program creates a Python dictionary that maps the sender's mail address to #
# a count of the number of times they appear in the file. After the dictionary is#
# produced, the program reads through the dictionary using a maximum loop to find#
# the most prolific committer.                                                   #
#********************************************************************************#
fname = raw_input("Enter file name: ") # prompts use to enter file name string
fh = open(fname) # opens and reads the file name.
counts = dict() # invoking a dictionary
for line in fh: #
    nospln=line.rstrip()# stripping \n character at end of line.
    if nospln.startswith("From ") : # finding the exact line required
        words=nospln.split() # splitting the words
        if words[1] in counts : # checking availability in dictionary
            counts[words[1]]=counts[words[1]]+1 # counter increases
        else :
            counts[words[1]] = 1 # if word not available assigns count as 1
bigcount = None
bigword = None
for word,count in counts.items():# applying for loop for Key- Value pairs
    if bigcount is None or count > bigcount:# checking big counter
        bigword = word # assigns word to respective variables.
        bigcount = count # 
print bigword,bigcount
