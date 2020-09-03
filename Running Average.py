N = int(input())
runner = list(map(int, input().split()))
total = 0
count = 1
for i in runner:
    total += i
    avg = total/count
    print(avg)
    count += 1