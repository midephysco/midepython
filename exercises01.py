#a program to write a function which inputs the names of two football teams
#and the score of each team 
def team():
	Teamone = input("please enter the name of your team")
	Teamtwo = input("please enter the name of your team")
	Teamonescores = input("Enter your score for {0}".format(Teamone))
	Teamtwoscores = input("Enter your score for {0}".format(Teamtwo))

	if Teamonescores > Teamtwoscores:
		print("{0} has 5 points while {1} has 0 point".format(Teamone,Teamtwo))
	elif Teamtwo > Teamone:
		print("{0} has 5 points while {1} has o points".format(Teamtwo,Teamone))
	else:
		print("Both {0} and {1} has same points".format(Teamone,Teamtwo))
team()