print("Squared of Numbers")
print("This program ask the user for a Number and the prints out the square")
print()
Number = int(input("Please enter a number: "))
print()
for Number in range(Number+1):
	print("{0} Squared is {1}.".format(Number,Number*Number))