# declaring the function here
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print "You have %d cheeses!" % cheese_count
    print "You have %d boxes of crackers!" % boxes_of_crackers
    print "Man that's enough for a party!"
    print "Get a blanket.\n"


# calling function directly with values
print "We can just give the function numbers directly:"
cheese_and_crackers(20, 30)

# initializing variables 
print "OR, we can use variables from our script:"
amount_of_cheese = 10
amount_of_crackers = 50

# passing variables as arguments to functions
cheese_and_crackers(amount_of_cheese, amount_of_crackers)


# statements as arguments 
print "We can even do math inside too:"
cheese_and_crackers(10 + 20, 5 + 6)


# statements and variables together as arguments
print "And we can combine the two, variables and math:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)
