x=str(input())
r=list()
cnt_l=cnt_r=cnt=0
pos=0
for i in range(0,len(x)):
    if(x[i]=='L'):
        cnt_l+=1
    else:
        cnt_r+=1
    if(cnt_l==cnt_r):
        cnt=cnt+1
        s1=str()
        for k in range(pos,i+1):
            s1+=x[k]
        r.append(s1)
        cnt_l=0
        cnt_r=0
        p=i+1
print(cnt)
for l in r:
    print(l)