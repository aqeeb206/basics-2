#exercise__1
# def CheckDriverAge(age='0'):
#     #age = input("What is your age?: ")

#     if int(age) < 18:
#         print("Sorry, you are too young to drive this car. Powering off")
#     elif int(age) > 18:
#         print("Powering On. Enjoy the ride!");
#     elif int(age) == 18:
#         print("Congratulations on your first year of driving. Enjoy the ride!")
# CheckDriverAge()        

#1. Wrap the above code in a function called checkDriverAge(). Whenever you call this function, you will get prompted for age. 
# Notice the benefit in having checkDriverAge() instead of copying and pasting the function everytime?

#2 Instead of using the input(). Now, make the checkDriverAge() function accept an argument of age, so that if you enter:
#checkDriverAge(92);
#it returns "Powering On. Enjoy the ride!"
#also make it so that the default age is set to 0 if no argument is given.

#EXERCISE ___2
def highest_even(li):
    evens=[]
    for items in li:
        if items%2==0:
            evens.append(items)
    return max(evens)    

              

        
print(highest_even([8,1,2,6,9,10,18]))
