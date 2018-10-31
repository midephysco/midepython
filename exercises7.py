import math
#a program that will calculate how far north and how far east a plane travelled at each point
distanceTravelled= float(20)
degreesFromNorth= float(60)
#north distanceTravelled
sineDegrees = 90 - degreesFromNorth
print("sineDegrees is {0} ".format(sineDegrees))
#convert the degrees to radians
sineRadians = math.radians(sineDegrees)
#find the  sine
sine = math.sin(sineRadians)
print("sine is {0} ".format(sine))
#distance north travelled
distanceNorth = round(sine * distanceTravelled,2)
#distance east 
sineRadians = math.radians(degreesFromNorth)
#solving for sine
sine = math.sin(sineRadians)
#distance east travelled
distanceEast = round(sine * distanceTravelled,2)
print("\nThe plane has travelled {0} north.".format(distanceNorth))
print("\nThe plane has travelled {0} east.".format(distanceEast))
