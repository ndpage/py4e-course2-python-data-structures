# Week 5 chapter 9  - Dictionaries
# Key Value pair data structure

# Referred to as 
#   Associative array - Perl/PHP
#   Properties/Map/HashMap - Java
#   Property Bad - C#/.NET

# Dictionary is like a mini database

dict1 = {'key1':3, 'hat':41, 'door':10}

val = dict1.get('hat',0) # this 1 line replaces if else statement to get key value

print("Value is:",dict1.get('key1',0))

print(dict1.items())  # Returns a list (array) of all items in form of a 2-tuple (cluster)
print(dict1.keys()) # Returns a list (array) of the keys

print(dict1.popitem()) # Removes (pops) the last key value pair from the dict
print(dict1.items()) # Returns a list (array) of all items in form of a 2-tuple (cluster)

for keys,vals in dict1.items(): # Python can have 2 iteration variables in a For loop when working with dictionaries
    print(keys,vals)