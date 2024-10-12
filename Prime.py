x=int(input("Enter num:"))
l=False
if x==1:
    print("not prime")
elif x>1:
    for i in range(2,x):
        if(x%i)==0:
            l=True
            break


if l:
    print("is not prime ")
else:
    print("is prime")
