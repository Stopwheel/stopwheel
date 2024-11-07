def add(a,b):
    return a+b
def sub(a,b):
    return a-b

def run(func,a,b):
    return func(a,b)

k=run(add,10,20)
print("k=",k)
print(run(sub,100,10))
print(run(lambda a,b:a*b,4,5))
print(run(lambda a,b:a/b,4,5))