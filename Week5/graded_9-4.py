# 9.4 Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail messages. 
# The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. 
# The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file. 
# After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.

fname = "../mbox-short.txt"
fhandle = open(fname)

textDict = dict()

# Step 1: Parse text and add email addresses to dictionary
for line in fhandle:
    if not line.startswith('From '): # Only keep the lines that start with 'From '
        continue
    list = line.split() # Split string in to a list (array)
    if len(list) < 1:  # Ignore empty lists
        continue
    textDict[list[1]] = textDict.get(list[1],0)+1 # add the email address and update the count

# Step 2: determine highest count email address (i.e. the greatest contributor)

maxCount = None # init variables to use for tacking max count
maxContributor = None
for person,count in textDict.items(): # iterate through each dict item
    if maxCount == None or maxContributor == None: # executes only on first iteration 
        maxContributor = person
        maxCount = count
    if count > maxCount: # update variables when new max count if found
        maxContributor = person
        maxCount = count

print(maxContributor, maxCount)