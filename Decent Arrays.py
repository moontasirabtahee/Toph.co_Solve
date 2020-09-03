N = int(input())
array = list(map(int,input().split()))
sorter = sorted(array)
if array == sorter:
    print('Yes')
else:
    print("No")