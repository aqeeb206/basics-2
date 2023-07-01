#  *args and **kwargs (arguments and keyword arguments)
# def super_func(*args, **kwargs):
#     #IT WILL ONLY TAKE ONE ARGUMENT 
#     #FOR MANY ARGUMENTS WE HAVE TO USE *args.
#     print(kwargs)
#     return sum(args)

    
# #print(super_func(1,2,3,4,5))  
#  #*kwargs it takes keyword arguments
#  #like
# print(super_func(1,2,3,4,5,num1=5,num2=10))
def super_func(*args,**kwargs):
    total=0
    for items in kwargs.values():
        total+=items
    return sum(args)  + total
print(super_func(1,2,3,4,5,num1=5,num2=10))  
#RULE FOR ORDERING FOR PARAMETES
# params,*args,i='hi,**kwargs
# example    def super_func(name, *args, i='hi', **kwargs):   