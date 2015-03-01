# line is just a string with %d
x = "There are %d types of people." %10
# line is a initialization
binary = "binary"
# yet another initialization
do_not = "don't"
#string with 2 valuse from %s
y = "Those who know %s and those who %s." %(binary, do_not)

# print string variables x and y
print x
print y

# another example of string formatter, introduction to %r
print "I said: %r." % x
print "I also said: '%s'." % y

# variable initialization hilarious as false
hilarious = True
# string variable initialization with a %r in the string
joke_evaluation = "Isn't that a joke so funny?! %r"

#printing joke_evaluation and adding hilrious to it using %r in joke_evaluation
print joke_evaluation % hilarious

# next to strings declared
w = "This is the left side of..."
e = "a string with a right side."

# concatenate the two strings using +
print w + e
