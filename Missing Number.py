given_total = int(input())
numbers = sum(list(map(int,input().split())))
last_number = given_total-numbers
print(last_number)