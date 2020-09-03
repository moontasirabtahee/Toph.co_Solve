N1,N2 = map(int,input().split())
set1 = set(map(int,input().split()))
set2 = set(map(int,input().split()))

output = sorted(list(set1.union(set2)))

for i in range(len(output)):
    if i == len(output)-1:
        print(output[i],end="")
    else:
        print(output[i],end=" ")