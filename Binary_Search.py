

list=[10,20,30,40,50,60,70,80,90,100,200,300,400,500,600,700,800,900,1000]




len=len(list)
pos=-1
l=0
u=len-1
x=0
n=int(input('Enter Key value:'))

while l<=u:
    #Find Mid Values Formula------------(lower+upper)//2
    mid=(l+u) // 2
    #compare list of mid and key value
    if list[mid] == n:
        #After Match Position Can Store
        x=1
        pos=mid
        #My key Value is Found Break loop and if
        break
    #Cannot match both values can enter else block
    else:
        #check list of mid value < lessthan key value
        if list[mid] < n:
            #True
            #lower can shift Mid place
            l=mid
        else:
            # if can False
            #upper can shift Mid place
            u=mid



if x==1:
    #After Break if block and loop display key value in  at position
    print(f'{n} is Found',pos+1,' Position')

else :
    print(n,'is Not found in Any Position')