N = int(input())
if N%4==0 :
    if N%100 ==0 and N%400 != 0:
        print("No")
    else:
        print("Yes")
else:
    print("No")