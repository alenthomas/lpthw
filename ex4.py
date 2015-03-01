#added variable car with value 100
cars = 100
#added variable space_in_a_car with value 4 in floating point
space_in_a_car = 4.0
#added variable drivers with value 30
drivers = 30
#added variable passengers with value 90
passengers = 90
#added varialbe cars_not_driven with value 100 - 30
cars_not_driven = cars - drivers
# assigned variable cas_driven with value drivers
cars_driven = drivers
# assigned variable carpool_capacity with value 30*4
carpool_capacity = cars_driven * space_in_a_car
# added variable average_passengers_per_car with value 90/30
average_passengers_per_car = passengers / cars_driven


print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."
