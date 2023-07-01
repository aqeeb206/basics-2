# def sum(num1,num2):
#     return num1 + num2
def sum(num1,num2):
    def anotherfunction(n1,n2):
       return n1 + n2
    return anotherfunction(num1,num2)
#return keyword automatically exits the function.    
    print('hello')   
total=sum(10,20)    
print(total) 