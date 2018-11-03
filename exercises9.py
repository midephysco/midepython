#a function that ask the user to enter a number between 1 and 20
def main():
	User = int(input("Please enter any number between 1 and 20 "))
	if User > 20:
		print("{0} is outside the given range".format(User))
	elif User < 1:
		print("{0} is lower than the range".format(User))
	else:
		print("{0} must be your favorite number".format(User))
main()