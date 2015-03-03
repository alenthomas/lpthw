#import module argv
from sys import argv

#initialize the argv as script and filename
script, filename = argv

#open the file and load it into txt
txt = open(filename)

#display the file name
print "Here's your file %r:" % (filename)
#read the contents of txt using read() and print it 
print txt.read()

#get the filename as a raw_input()
print "Type the filename again:"

# get the name of the file as raw_input() and give it to file_again
file_again = raw_input("> ")

# open the file_again and give it to txt_again
txt_again = open(file_again)

# read the contents of txt_again using read() and print
print txt_again.read()
