
# Strings are objects. Use type command and returns "str"
#
# use dir(object) to get the available methods for that object
#   .lower() -> returns a lower case copy of the string

stringVar = "this is a string"
index = 0
#while index < len(stringVar):
#  print("current letter:",stringVar[index])
#  index = index + 1
#print("number of letters:",index)
count=0
for letter in stringVar:
  print("current letter:",letter)
  count = count + 1
print("number of letters:",count)

print(stringVar[0:3])

# using "in" as a logical operator
while False:
  strInput = input("Enter search character: ")
  if strInput == "exit":
    break
  found = strInput in stringVar

  found = str(found) # convert to string object to use .upper() method

  print("found->",found.upper())

# stripping whitespace

whitespace  = '   hello    '
print(whitespace.lstrip()) # left strip
print(whitespace.rstrip()) # right strip
print(whitespace.strip()) # strip all whitespace
