# #Exercise! GUI
# #Display the image below to the right hand side where the 0 
# #is going to be ' ', and the 1 is going to be '*'. 
# #This will reveal an image!
# picture = [
#   [0,0,0,1,0,0,0],
#   [0,0,1,1,1,0,0],
#   [0,1,1,1,1,1,0],
#   [1,1,1,1,1,1,1],
#   [0,0,0,1,0,0,0],
#   [0,0,0,1,0,0,0]
# ]

# for row in picture:
#   for pixels in row:
#     if(pixels==0):
#       print(" ",end=' ')
#     else:
#       print("*",end=' ')
#   print()    

#exercise print duplicates
some_list=['a','b','c','d','e','b','n','m','n']
duplicates=[]
for value in some_list:
  if some_list.count(value)>1:
    if value  not in duplicates:
      duplicates.append(value)
print(duplicates)      
   
   