data=list(map(int,input().split(",")))
max_val=data[0]
min_val=data[0]
total=0
n=0
for x in data:
    if x>max_val:
        max_val=x
    if x<min_val:
        min_val=x
    total+=x
    n+=1
print(f"max:{max_val}")
print(f"min:{min_val}")
print(f"{total}")
print(f"{total/n}")