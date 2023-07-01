#TRUTHY AND FALSY
username='hello'
password=55
#the above 2 values of variable will be converted to boolean values.
#example bool('hello') and bool(55)
#these two values will become 1 and will be called as truthy value.
#EXAMPLES OF TRUTHY VALUE
print(bool('hello')) #--> 1=True
print(bool('55'))    #--> 1=True
#FALSY VALUE
print(bool(''))#--> 0=False
print(bool(0))#--> 0=False
if username and password:
    print('you are old enough to drive and you have license to drive')
else:
     print('you are not eligible to drive!')
#ALL VALUES ARE  CONSIDERED 'TRUTHY' EXCEPT FOR THE FOLLOWING , WHICH ARE FALSY 
# eg-: None , False ,0 , 0.0, 0j,an empty list[] or set{},search google for more value.      