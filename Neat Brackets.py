n  = input()
dashes = [x for x in n if x in ["(",")"]]

start = 0
end = 0
fla = False
for i in dashes:
    if i == "(":
        start+=1
    elif i == ")":
        end +=1

    if start < end:
        fla = True
        break

if fla == False and start == end :
    print("Yes")
else:
    print("No")
