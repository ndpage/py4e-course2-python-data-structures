# Open files
# open(filename,mode) gets a reference to a file 
# Other methods: read(), write(), and close()



string = "abc"
integer = 1
floating = 1.11
boolean = True

cluster = (string, integer, floating, boolean)

print(type(cluster))

for each in cluster:
  print(each)

# for item in cluster:
#   print(type(item))
#   methods = dir(item)
#   for method in methods:
#     print(method)
  
