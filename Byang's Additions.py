first,second = map(int,input().split())
flag = 0
while(first != 0 and second != 0):
    temp1 = first%10
    temp2 = second%10

    if (temp1+temp2>9):
        flag += 1
        break

    first/=10
    second/=10

if flag == 0:
    print("No")
else:
    print("Yes")