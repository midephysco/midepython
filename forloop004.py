password = ""
while password != "secret":
	password = input("Please enter your password: ")
	if password== "secret":
		print("Thank you. You have entered the correct password")
	else:
		print("Sorry the value entered is incorrect")


