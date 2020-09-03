number,cpul ,meml = map(int,input().split())

test = []
for i in range(number):
    checkcpu,checkmem,checkwa = 0,0,0
    di ,cpu ,mem = map(int,input().split())
    if di != 0 :
        checkwa +=1
    if cpu > cpul:
        checkcpu +=1
    if mem > meml:
        checkmem +=1

    if checkcpu == 1 :
        test.append("CLE")
    elif checkmem == 1:
        test.append("MLE")
    elif checkwa == 1:
        test.append("WA")
    else :
        test.append("AC")
setin = False
for i in test:
    if i != "AC":
        setin = True
        print(i)
        break
if setin == False:
     print("AC")