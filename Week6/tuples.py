# Week 6 - Tuples
# Tuples are a collection of items. The main difference between tuples and 
#  Lists is that tuples are immutable


tup = (3,5,11)

print(tup)

l = [] # List
d = {'a':2,'c':5,'b':1,'f':12} # Dictionary
t = ('hey','tue','wed',0.21,d) # Tuple

print(sorted(d.items())) # gets items in dictionary, sorts them, and then prints the result

# List comprehension in Python
print(sorted([(v,k) for k,v in d.items()])) # <-- list comprehension: [(expression) for (value) in (collection) if (condition)]

