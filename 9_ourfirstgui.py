# Exercise!
# Display the image below to the right hand side where the 0 is going to be ' ', and the 1 is going to be '*'. This will reveal an image!
# picture = [
#     [0, 0, 0, 1, 0, 0, 0],
#     [0, 0, 1, 1, 1, 0, 0],
#     [0, 1, 1, 1, 1, 1, 0],
#     [1, 1, 1, 1, 1, 1, 1],
#     [0, 0, 0, 1, 0, 0, 0],
#     [0, 0, 0, 1, 0, 0, 0]
# ]
# # 1 iterate over picture
# for image in picture:
#     for pixels in image:
#         if (pixels == 1):
#             print('*', end=" ")
#         else:
#             print(" ", end=" ")
#     print('\n')
#FINDING DUPLICATES
some_list=['a','b','c','d','m','n','n']
duplicates=[]
for char in some_list:
    if some_list.count(char) > 1:
        if char not in duplicates:
          duplicates.append(char)
print(duplicates)        
#another way.

some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']

some_list2 = []

for i in some_list:
    if i not in some_list2:

      some_list2.append(i)

    else:

       print(i)