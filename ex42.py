## Animal is-a object (yes, sort of confusing) look at the extra credit
class Animal(object):
    pass

## Dog has-a an object of type Animal
class Dog(Animal):

    def __init__(self, name):
        #Dog has-a __init__ function that has a variable name
        self.name = name

#cat has-a object of type Animal
class Cat(Animal):

    def __init__(self, name):
        ## Cat has a __init__ function that takes self and name as parameters
        self.name = name

## Person is an object
class Person(object):

    def __init__(self, name):
        ## instatiate Person with a variable name as name
        self.name = name

        ## Person has-a pet of some kind
        self.pet = None

## Employee is-a class of type Person
class Employee(Person):

    def __init__(self, name, salary):
        # create an object of type Employee ?? i think
        super(Employee, self).__init__(name)
        ## set value to attribute of Employee as salary
        self.salary = salary

## Fish is a object 
class Fish(object):
    pass

## Salmon is a class of type Fish
class Salmon(Fish):
    pass

## Halibut is a class of type Fish
class Halibut(Fish):
    pass


## rover is-a Dog
rover = Dog("Rover")

## satan is-a Cat
satan = Cat("Satan")

## mary is-a person
mary = Person("Mary")

## mary has a variable pet set as satan
mary.pet = satan

## frank is-a employee with salary attribute set as 120000
frank = Employee("Frank", 120000)

## frank has a variable pet set as rover
frank.pet = rover

## flipper is an object of type Fish()
flipper = Fish()

# crouse is an object of type Salmon()
crouse = Salmon()

## harry is an object of type Halibut()
harry = Halibut()
