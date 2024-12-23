import math
a=int(input("請輸入科目一的成績:"))
b=int(input("請輸入科目二的成績:"))
c=int(input("請輸入科目三的成績:"))
d=int(input("請輸入科目四的成績:"))
u=(a+b+c+d)/4
formatted_u="{:.2f}".format(u)
ans=((a-u)**2+(b-u)**2+(c-u)**2+(d-u)**2)/4
f=math.sqrt(ans)
print("平均成績為:",formatted_u)
print("成績標準差為:",round(ans,2))