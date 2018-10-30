#a program that tels the user to enter 3 numbers
# and then multiply the first two and dividing the output by the third number
firstnumber= input("please enter a number ")
secondnumber = input("please enter a number")
thirdnumber = input("please enter a number")
multiply = int(firstnumber) * int(secondnumber)
#we now divide the output by the third number
div = int(multiply) / int(thirdnumber)
print("The answer is {0}".format(div) )