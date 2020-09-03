
N= input()
flag = 1
checker =[0]
for i in N:
    if i =="(" or i =="{" or i == "[":
        checker.append(i)
    else:
        if i  == ")":
            if checker[-1] == "(":
                checker.pop()
            else:
                flag = 0
                break
        elif i == "]":
            if checker[-1] == "[":
                checker.pop()
            else:
                flag = 0
                break
        elif i == "}":
            if checker[-1] == "{":
                checker.pop()
            else:
                flag = 0
                break

if checker[-1] != 0 :
    flag = 0

if flag:
    print("Yes")
else:
    print("No")

