numbers = []
limit = int (raw_input("Enter limit: "))
inc = int ( raw_input("Enter incremet value: "))
def whil(var, up):
    i = 0
    while i < var:
        print "At the top i is %d" % i
        numbers.append(i)

        i = i + up
        print "Numbers now: ", numbers
        print "At the bottom i is %d" % i


whil(limit, inc)
print "The numbers: "

for num in numbers:
    print num
