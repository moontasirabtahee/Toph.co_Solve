N = int(input())
for i in range(N):
    for j in range(N-i-1):
        print(end=" ")
    for j in range(i+1):
        if j != i:
            print("*",end=" ")
        else:
            print("*", end="")
    if i != N-1:
        print()
