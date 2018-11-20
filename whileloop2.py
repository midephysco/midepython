#continous loop
print("Adding until rogue value")
print()
print("This program adds up values until a rogue values is entered ")
print()
print("it then displays the sum of the values entered ")
print()
Value = None
Total = 0
while Value != 0:
	print("The total is: {0}.".format(Total))
	print()
	Value = int(input("Please enter a value to add to total: "))
	Total = Total + Value
print()
print("The final total is: {0}.".format(Total)) 
