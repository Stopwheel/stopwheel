a = int(input("x="))
n = 0
b = a // 1000 
c = (a % 1000)// 100 
d = (a % 100) // 10 
e = a % 10
while True:
    if b in [0, 1, 6, 8, 9]:
        n += 1
    if c in [0, 1, 6, 8, 9]:
        n += 1
    if d in [0, 1, 6, 8, 9]:
        n += 1
    if e in [0, 1, 6, 8, 9]:
        n += 1
    break
if n == 4:
    print("True")
else:
    print("False")