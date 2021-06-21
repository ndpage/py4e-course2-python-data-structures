# Open files
# open(filename,mode) gets a reference to a file 
# Other methods: read(), write(), and close()

fhandle = open("test.txt")

# new line character \n
# New line does not get shown but exist in most files

for each_line in fhandle:
    each_line = each_line.rstrip()
    if not each_line.startswith("This"):
        continue
    print(each_line)
    
