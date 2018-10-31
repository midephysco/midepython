#this program will calculate the volumw of a fridge and a lift 
#with an assumed parameter heights, widths and depths
#and also Work out how much space is left in the lift once the fridge is inside
def main():
	#enter parameter for the fridge
	fridgeheight= input("enter a number ")
	fridgewidth= input("enter a number ")
	fridgedepth= input("enter a number")
	#parameters for the lift
	liftheight= input("enter a number ")
	liftwidth= input("enter a number ")
	liftdepth= input("enter a number")
	#volume for the fridge
	fridgevolume = int(fridgeheight) * int(fridgewidth) * int(fridgedepth)
	print("ans = {0}".format(fridgevolume))
	#volume for the lift
	liftvolume = int(liftheight) * int(liftwidth) * int(liftdepth)
	print("ans = {0}".format(liftvolume)) 
	thespace = liftvolume - fridgevolume
	print("the remainin g space is int({0})".format(thespace))
main()


