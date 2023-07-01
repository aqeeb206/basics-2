# #logical operator-->  (and , or , > , < , == , ! , >= , <= ,not)
# print(4==5)
# # why we have use double equal sign here?
# '''if we use single  eqaul sign here for example (4=5) 'error will be shown keyword cant be expression' and also 
# 'expression cannot contain assignment, perhaps you meant "=="?'g . bcoz '''
# print('apple')
# print('a'>'%')#ascii fundamentals # it is not that important but it would be better if we know it.
# print(1<2>3<4)
# print('hello'=='hello')
# print(1>=0) 
# print(1<=0)
# print(0<=0)
# print(0!=1)
# print(not([]))#not is used for the oposite true will get convert into false and vice versa.


# logical operators exercise

is_magician=False
is_expert=True
# check if magician and expert 
if is_magician and is_expert:
    print('you are a master magician')
#check if magician and not expert ..to use not it will be better instead of using or.   
elif is_magician and not is_expert:
    print('at least you are getting there') 
#if you are not a magician .     
else:
    print('you are not a magician')      
    #in programming there will be many ways to solve a problem but a key is to solve it in a simple manner and readable.
    