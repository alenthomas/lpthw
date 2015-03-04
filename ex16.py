from sys import argv

#set script and filename as argv types
script, filename = argv

# display the file to be erased and rewrite
print "We're going to erase %r." %( filename)
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want that, hit RETURN."

# just a raw_input to break the control from jumping to the next
raw_input("?")

#open file as a 'w'
print "Opening the file ..."
target = open(filename, 'w')

#truncate() is used to empty the file
print "Truncationg the file.  Goodbye!"
target.truncate()

#get the input from user 3 typical lines
print "Now I'm going to ask for three lines."

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to the file."

#write the lines to file with a newline between after every line
target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

#finally close the file
print "And finally, we close it."
target.close()
