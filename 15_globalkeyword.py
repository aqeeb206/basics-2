# a=10
# def confusion(b):
#     print(b)
#     a=90
# confusion(300)#parameters are considered local variables.  

# total=0
# def count():
#     total+=1
#     return total
# print(count())       
#O/P--ERROR LOCAL VARIABLE TOTAL REFERENCED BEFORE ASSIGNMENT.
# total=0
# def count():
#     global total
#     total +=1
#     return total

# count()
# count()
# print(count())
total=0
def count(total):
    total+=1
    return total
count(total) 
count(total) 
print(count(total))  
  #insted we can do something like this
  # print(count(count(count(total))))   
  # it will give answer 3 