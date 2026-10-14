n=int(input())
for row in range(0,n):
    for col in range(o,n):
        if row==0 or col==0 or row==n-1 or col==n-1:
            print("*",end=" ")
        else:
              