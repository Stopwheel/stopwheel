def draw(n,c):
    for i in range(n):
        for j in range(n-i-1):
            print(" ",end="")
        for j in range(2*i+1):
            print(c,end="")
        print()

if __name__=="__main__":
    n,c=input("Enter a number and a character:").split( )
    draw(int(n),c)