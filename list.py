num=input().strip()

rev=num[::-1].lstrip('0')

rev=rev if rev!='' else '0'
#print(rev)

if num==num[::-1] :
    print(rev)
    print('YES')
else:
    print(rev)
    print('NO')