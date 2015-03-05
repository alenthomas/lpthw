from sys import argv

script, input_file = argv

# function to read() a file
def print_all(f):
    print f.read()

# function to seek the file
def rewind(f):
    f.seek(0)

# print file line by line
def print_a_line(line_count,f):
    print line_count, f.readline()

# open the file
current_file = open(input_file)

print "First let's print the whole file:\n"

# print the whole file
print_all(current_file)

print "Now let's rewind, kind of like a tape."

# use seek to print file from beginning
rewind(current_file)

print "Let's print three lines:"

# set current_line as 1 and so on till line 3
# the current_line is used to print the line no 
# readline() inside print_a_line() prints line by line anyways
current_line = 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)
