class Parent(object):

    def implicit(self):
        print "PARENT implicit()"

class Child(Parent):
    def implicit(self):
        print "CHILD implicit()"
        super(Child, self).implicit()
        print "CHILD, AFTER PARENT altered()"

dad = Parent()
son = Child()

dad.implicit()
son.implicit()
