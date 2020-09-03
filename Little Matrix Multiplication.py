first = []
second = []
result = [[0,0],[0,0]]
for i in range(4):
    if i>1:
        temp = list(map(int,input().split()))
        second.append(temp)
    else:
        temp = list(map(int,input().split()))
        first.append(temp)

for i in range(len(first)):
   for j in range(len(second[0])):
       for k in range(len(second)):
           result[i][j] += first[i][k] * second[k][j]

for i in result:
    for j in i:
        print(j,end=" ")
    print()
