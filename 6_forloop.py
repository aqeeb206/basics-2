# for item in (1,2,3,4,5):
#     for x in ['a','b','c']:
        # print(item,x)
        #we can also have nested loops .
#ITERABLES
#iterable can be  a collection of list , set, dictionary,tuple,string 
# iterate -->one by one check each item  in the collection  .
users={
    'name': 'Golem',
    'age': 5006,
    'can_swim':False
}
for item in users:
    print(item)
  # it will only  print the keys of the dictionary.
  # there are also 3 ways to get key and value of a dictionary.
  #these 3 methods you will use a lot of in your career.
#1____way  to grab both keys and values
for item in users.items():
    print(item)   
#2____way    #to grab the values    
for item in users.values():
    print(item)   
#3____way #to grab keys    
for item in users.keys():
    print(item)    
'''another interesting way of doing this'''    
for item in users.items():
    key,value=item
    print(key,value)    
#another short hand way of doing this.
for key,value in users.items():
    print(key,value)
# for i in 50:
#     print(i)    
    #int object is not iterable .int is not a collection of items.
#tricky counter exercise
my_list=[1,2,3,4,5,6,7,8,9,10] 
counter=0 
for item in my_list:
    #make sure that you have the variable outside the loop
    #because if we keep the variable inside and initialise it with zero 
    #everytime the loop runs the counter resets to zero.
    counter+=item
    print(counter)
print(counter)  #to  get the final answer use the print outside the loop. 
tpple=(0,12,34)
print(dict(tpple))

