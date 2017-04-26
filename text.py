# open the file - and read all of the lines. 
changes_file = 'Changes_python.txt' 

# use strip to strip out spaces and trim the line. 

my_file = open(changes_file, 'r') 
data = my_file.readlines() 
data = [line.strip() for line in open(changes_file, 'r')] 

# print the number of lines 
print(len(data)) 
sep = 72*'-' 
