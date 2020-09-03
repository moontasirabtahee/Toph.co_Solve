N = int(input())
first = 0
second = 1
output = 0
if N == 1:
    print(0)
elif N ==2:
    print(1)
else:
    for i in range(1,N,1):
        output = first+second
        first = second
        second = output

    print(output)