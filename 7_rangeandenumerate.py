# print(range(100))
# #o/p-->range(0,10)
# for number in range(0,5):
#     print(number)
# for _ in range(0,10):#we can also use this (_) 
#     # instead of using a variable .
#     print('email email ')
# for _ in range(10,0,-1): #we get the reverse numbers.
#     print(_)  #third parameter is also known as a step over.
# #it wont work as (0,10,-1).have a note of it.
# for _ in range(2):
#     print(list(range(10)))#o/p-->\a list of 10 numbers will be generated.
#     #it is a neat trick that you will use along your programmer journey.
#   ENUMERATE
#enumerate is useful if you need the index counter of the item 
# that you are looping through.
for i,char in enumerate('hello'):
    print(i,char)    #o/p--> index of each char of hello word.  
#it also works for list,tuples as well.
#exercise of enumerate
for i,char in enumerate(list(range(1,100))):
    if char==50:
        print(f'index of 50 is: {i}')
      #not as useful as range but you will see it ocassionally.  