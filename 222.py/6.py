n,m=map(int,input().split())
total=0
if n>m:
    n,m=m,n
i=n
while i<=m:
    if i %2==1:
        total+=i
    i+=1
print(total)