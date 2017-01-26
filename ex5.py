my_name = "Zed"
my_age = 35 # not a lie
my_height = 74 # inches
my_weight = 180 # pounds
my_kilograms = my_weight / 2.20462
my_meters = float(my_height / 39.37)
my_eyes = "Blue"
my_teeth = "White"
my_hair = "Brown"

print my_meters

print "Let's talk about %s." % my_name
print "He's %d inches tall." % my_height
print "He's %d pounds heavy." % my_weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (my_eyes, my_hair)
print "His teeth are usually %s depending on the coffee." % my_teeth
print "My weight in kilograms is: %d" % my_kilograms
print "My height in meters is: repr(%d)" % my_meters

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % ( my_age, my_height, my_weight, my_age + my_height + my_weight)
