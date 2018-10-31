#math unit exercises
#a program to calculate the circumference and area of a circle
import math
radius= float(input("enter a value for radius"))
print("Radius is {0}".format(radius))
#now we want to calculate the area of a circle
Area=  round(math.pi * radius * radius,2)
print("Area of the circle is {0}".format(Area))
circumference= round(2 * math.pi * radius,2)
print("\nThe circumference of the circle is {0}".format(circumference))

