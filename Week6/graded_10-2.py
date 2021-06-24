# 10.2 Write a program to read through the mbox-short.txt
#    and figure out the distribution by hour of the day for each of the messages. 
# You can pull the hour out from the 'From ' line by finding the time
#    and then splitting the string a second time using a colon.
#       From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
# Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.

name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)
hrlist = list()
for line in handle: # read each line
  if not line.startswith('From '):  # extract lines that start with From
    continue
  wlist = line.split()    # split string into a list of strings 
  time = wlist[5]         # store time string in variable 'time'
  time = time.split(':')  # split time into a list of strings
  hrlist.append(time[0])

# determine occurance of each hour
count = dict()  # create count dictionary
for hr in hrlist:
   count[hr] = count.get(hr,0) + 1  # increment count for each hour in the dictionary

count = sorted(count.items()) # sort the items in the dictionary

[print(item[0],item[1]) for item in count] # print each hour and count in the sorted count dictionary