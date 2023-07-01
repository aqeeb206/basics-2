# if True:
#     x=10
# def some_func():
#     #when we create a new function we crate a new world  that anything thats indented inside
#     #inside of the function is its own world that we dont really have 
#     #access to 
#     # we can only use total if we indent print   inside of this world(function).    
#     total=100
# print(x)   
# SCOPE RULES     
a=1
# def confusion():
#     a=5
#     return a
# print(confusion())    
# print(a)
#1- start with a local
# a local scope is a scope thats part of this local function.
#2-- parent local scope .(is there a parent local scope)
#EXAMPLE:
def parent():
    def confusion():
       return a
    return confusion()   
print(parent())
print(a)    
#3--GALOBAL
#IF A DOESNT EXIST IN PARENT OR LOCAL THEN WE TAKE IT FROM GLOBAL
#4-- BUILT IN PYHTON functions.
#example
def parent():
    def confusion():
       return sum
    return confusion()   
print(parent())
print(a)  
#the interpreter will check in built in python functions.
# this is some of the rules that python interpreter follows.

