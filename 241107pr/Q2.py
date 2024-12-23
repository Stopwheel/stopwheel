def fibonacci_recursive(n):
    if n==1:
        return 0
    elif n==2:
        return 1
    else:
        return fibonacci_recursive(n-2)+fibonacci_recursive(n-1)
print(fibonacci_recursive(5))