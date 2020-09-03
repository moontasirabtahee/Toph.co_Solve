H,M = map(int,input().split())
theta  = abs((11/2)*M-(30*H))
ans = min(360-theta,theta)
print("%.5f"%ans)