#***********************************************************************************
#7.2 Write a program that prompts for a file name, then opens that file and reads
#through the file, looking for lines of the form:
#X-DSPAM-Confidence:    0.8475
#Count these lines and extract the floating point values from each of the lines and
#compute the average of those values and produce an output as shown below.
#Do not use the sum() function or a variable named sum in your solution.
#You can download the sample data at http://www.pythonlearn.com/code/mbox-short.txt
#when you are testing below enter mbox-short.txt as the file name.
#***********************************************************************************


fname = raw_input("Enter file name: ") # prompts for input file name text
fh = open(fname) # opens and reads the supplied file name from the current working directory
count = 0 # count initializer statment
ftotal=0.0 # flot value total initializer statment
for line in fh: #for loop for extracting required float value for each line
    line = line.rstrip() # to strip \n for every new line.
    if line.startswith("X-DSPAM-Confidence:") :# checking each line startswith if not goes  top of loop
        count=count+1 # Count increases
        index=line.find(":") # finding the specfic known pattern index in string
        value=line[index+1 : (len(line))]# extrating the required float value string portion with spaces
        value=value.strip()# using string statment for stripping of left and right spaces if any
        fvalue=float(value) # converting string type to float
        ftotal=ftotal+fvalue # adding converted float value to initialized variable
    else : continue
result= (ftotal/count)# finding Average
print 'Average spam confidence:', result # printing result 
