people = 30
cars = 40
trucks = 15

# if condition evaluates to true it executes the block under it
if cars > people:
    print "We should take the cars."
# else it checks for another if and executes the code block under it
elif cars < people:
    print "We should not take the cars."
# this executes if the above if condition fails
else:
    print "We can't decide."

if trucks > cars:
    print "That's too many trucks."
elif trucks < cars:
    print "Maybe we could take the trucks."
else:
    print "We still can't decide."

if people > trucks:
    print "Alright, let's just take the trucks."
else:
    print "Fine, let's stay home then."
