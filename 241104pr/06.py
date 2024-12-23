def fun(n):
    if n==1:
        return 0
    elif n==2:
        return 1
    else:
        return fun(n-2)+fun(n-1)
print(fun(6))