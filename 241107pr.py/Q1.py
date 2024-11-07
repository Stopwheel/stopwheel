def factorial_recursive(n):
    if n == 0:
            return 1
    else:
        val=1
        for i in range(n,1,-1):
            val*=i
        return val
print(factorial_recursive(5))