#this is a program to enter 2 numbers and output the remainder
n0 = input("enter a number ")
n1 = input("enter another number")
div = int(n0) / int(n1)
remainder = int(n0) % int(n1)
print("the answer is {0} remainder {1}".format(div, remainder))