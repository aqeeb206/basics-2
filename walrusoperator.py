a='helloooooooo'
if(len(a)>10):
    print(f'too long {len(a)} element')
if ((n:=len(a))>10):
    print(f'too long {n} element') 
print(n)       
while ((n:=len(a))>1):
    print(n)
    a=a[:-1]
print(a)       