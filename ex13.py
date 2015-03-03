from sys import argv

script, first, second, three, four  = argv

#print "The script is called:", script
print "Your first candidate is :", first
#print "Your second variable is:", second
#print "Your third variable is:", three
#print "Your fourth variable is:", four

print "\nEnter details of %r age, height" %(first),
age = int(raw_input())
height = int(raw_input())

print "\n So candidate  %r with age %s and height %s" %( first, age, height)
