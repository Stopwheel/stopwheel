data=[]
while True:
    a=input()
    if a == -999:
        break
    a=float(a)
    i=0
    while i < len(data) and data[i]<a:
        i+=1
    if i == len(data):
        data.append(a)
    else:
        data.insert(i,a)
    