n=int(input())
mid=n//2
for row in range(0,n):
    for col in range(0,n):
        if col==0:
            print("*",end=" ")
        elif row==mid:
            print("*",end=" ")
        elif col==n-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()