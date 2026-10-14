n=int(input())
mid=n//2
for row in range(0,n):
    for col in range(0,n):
        if row==0:
            print("*",end=" ")
        elif col==mid:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()