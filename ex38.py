ten_things = "Apples Oranges Crows Telephone Light Sugar"

print "Wait there are not 10 things in that list. Let's fix that."

stuff = ten_things.split(' ')
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

while len(stuff) != 10:
    next_one = more_stuff.pop()
    print "Adding: ", next_one
    stuff.append(next_one)
    print "There are %d items now." % len(stuff)

print "There we go: ", stuff

print "Let's do some things with stuff."

print stuff[1]
# '-' indexes print lists backwards
print stuff[-1] # whoa! fancy
print stuff.pop()
# join(list)  concatenates lists to strings with the given parameter
#            in this case its a space
print' '.join(stuff) # what? cool!
# join items from indexes 3 and 5 with a # symbol
print '#'.join(stuff[3:5]) # super stellar!
