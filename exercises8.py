#Write a function that asks the user how old they are. 
def vot():
	Age = int(input("How old are you? "))
    #also to tell the user if they are old enough to vote.
    if Age >= 18:
    	print("you are old enough to vote")
    else:
        Age < 18
        print("you are too young to vote, kindly wait till you are 18")
    #extend the program to tell them how many years it is until they can retire (assume at age 65).       
    print("ageToRetire is 65 ")
    if Age < 65:
        ageToRetire = 65 - Age
        print("You can retire in {0} years.".format(ageToRetire))
vot()  
        
    
 
