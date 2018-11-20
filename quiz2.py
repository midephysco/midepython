def quiz():
	print("Here's is a quiz to test your knowledge of farming...")
	print()
	print()
	print("This week has a farming theme so we need to see what you know already about farms")
	print()
	print("Question 1")
	print("What percentage of land is used for farming? ")
	print()
	print("a...25%")
	print("b....50%")
	print("c...75%")
	print()
	choice = input("Make your choice: ")
	if choice == 'c':
	    print("Correct!")
	elif choice == 'b':
		print("Please try again")
	elif choice == 'a':
		print("You have exhausted you chances!")
	else:
		print("The correct option is c!")
quiz()

	
quiz()
