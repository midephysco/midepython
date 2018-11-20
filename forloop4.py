#a program that calculate the average mean of a set of numbers
#the user is asked of how many numbers are to be averaged
#this progarm will calculate and show the average of those numbers.

def ave():
	numbers = int(input("How many numbers do you want to be averaged?"))
	Total = 0
	for count in range(numbers):
		nextNumber = int(input("Enter the next number"))
		Total = Total + nextNumber
	average = Total/numbers
	print("The mean of your numbers is {0}.".format(average))
ave()
