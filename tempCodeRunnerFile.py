def highest_even(li):
    is_even=[]
    for i in li:
        if i%2==0:
            is_even.append(i)
        
    return max(is_even)     
print(highest_even([1,2,3,4,4962,56,11]))