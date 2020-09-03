N = int(input())
for i in range(N):
    num1,num2 = map(int,input().split())
    avg = (num1+num2)//2

    if avg%2==0:
        print('Sadia will be happy.')
    else:
        print('Oops!')