

a=[1,20,50,3,79,48,75,7,8]

len=len(a)
print(len)
val=int(input('Enter Number You Want to Search :'))
 
i=0
key=0
while i<len:
    if a[i] == val:
        print(a[i],'is Found')
        key=1
        break
     
    
    i=i+1

if key ==0:
    print(val,'is Not Found')

    
