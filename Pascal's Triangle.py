N = int(input())-1
prev = 1
lastrow = []
lastrow.append(prev)
for i in range(1,N+1):
    curr = (prev * (N - i + 1)) // i
    lastrow.append(curr)
    prev =curr


print(sum(lastrow))