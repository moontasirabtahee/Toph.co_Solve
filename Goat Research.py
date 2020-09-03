num = int(input())
baa =[]
max = 0
for i in range(num):
    string = input()
    a=string.count("a")
    if a == 1:
        string+="a"
    elif a%2 != 0:
        string = string[:-1]
    else:
        pass
    if len(string)>max:
        max = len(string)

    baa.append(string)

for i in range(num):
    space = (max - len(baa[i]))//2

    for j in range(0,space,1):
        print(" ",end ="")
    print(baa[i])