T = int(input())
for i in range(T):
    ball = input()
    counter =0
    for x in ball:
        if x in ['0','1','2','3','4','5','6']:
            counter+=1
    over = counter // 6
    balls = counter%6
    if over > 1 and balls > 1:
        print("{} OVERS {} BALLS".format(over,balls))
    elif over == 1 and balls == 1:
        print("{} OVER {} BALL".format(over,balls))
    elif over == 0 and balls>1:
        print("{} BALLS".format(balls))
    elif over ==0 and balls==1:
        print("{} BALL".format(balls))
    elif over > 1 and balls ==0:
        print("{} OVERS".format(over))
    elif over == 1 and balls == 0:
        print("{} OVER".format(over))
