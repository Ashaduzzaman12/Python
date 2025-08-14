x=int(input())
cnt=0
l=list(map(int,input().split()))
m={}
for i in range(0,len(l)):
    m[l[i]]=m.get(l[i],0)+1
for i in m:
    if i<m[i]:
        cnt+=m[i]-i
    elif i>m[i]:
        c+=m[i]
print(c)