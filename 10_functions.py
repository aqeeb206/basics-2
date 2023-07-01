#FUNCTIONS 
#to define a function use def followed by the name you want to give and a colon at laast.
#Deafault parameters
# it is what we want as a default parameter when we define the funcction.
def say_hello(name='Darth vader ',emoji='😂'):
    print(f'hell0 {name} {emoji}')

# def say_hello(name,emoji):
#     print(f'hell0 {name} {emoji}')
picture = [
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 1, 1, 1, 0, 0],
    [0, 1, 1, 1, 1, 1, 0],
    [1, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0]
]
def showtree():
    for image in picture:
        for pixels in image:
            if (pixels == 1):
                print('*', end=" ")
            else:
                print(" ", end=" ")
        print('\n')

#so parameters are used when we define the function and arguments are used when we call the function.
#ARGUMENTS are used as the actual value we provide to a function. 
# POSITIONAL ARGUMENTS  
# poistional arguments are alos     
say_hello('Aqeeb', 'smile')    
say_hello('Aqu', 'laugh ')  
#KEYWORD ARGUMENTS
say_hello(emoji='cry',name='dan')      
#its a bad practice . you can use keyword arguments but make sure they are in order in which they are in function.
#print(showtree()) 
#print(showtree())  
#print(showtree)#it will give the location of the function in memory.
say_hello()