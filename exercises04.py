#Ask the user to enter the current month, the program should output whether the month is in Winter, Spring, Summer or Autumn.
def user():
    prompt = input("what month are we in? ")
    print("We are in {0},the 11**th month of the year ".format(prompt))
    if prompt == "November":
    	print("we're in Autumn season")
    else:
    	print("it's not yet Autumn ")
user()