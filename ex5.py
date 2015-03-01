name = 'Alen Thomas'
age = 21 #going to be 22 soon
height = 65 #inches
weight = 65 #kg
eyes = 'Black'
teeth = 'White'
hair = 'Black'

# 1 cm = 0.39370 inch
# 1 inch = 2.5400 cm

height_to_cm = height * 2.5400

# 1 pound = 0.45359 kg
# 1 kg = 2.2046 pounds

weight_to_pound = weight * 2.2046

print "Let's talk about %s." % name
print "He's %d cms tall." % height_to_cm
print "He's %d pounds heavy." % weight_to_pound
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." %(eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." %( age, height_to_cm, weight_to_pound, age + height_to_cm + weight_to_pound)
