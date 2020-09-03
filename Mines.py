R, C = map(int ,input().split())
field = []
for i in range(R):
    temp = [i for i in input()]
    field.append(temp)
mat = [[0 for i in range(C)] for i in range(R)]
count = 0
for r in range(R):
    for c in range(C):
        ans = 0
        if field[r][c] == ".":
            if r == 0 and c == 0:
                if field[c+1][r+1] == "*":
                    ans+=1
                if field[c][r+1] == "*":
                    ans+=1
                if field[c+1][r] == "*":
                    ans += 1
            elif r == R-1 and c == 0:
                if field[r-1][c+1] == "*":
                    ans +=1
                if field[r-1][c] == "*":
                    ans += 1
                if field[r][c+1] == "*":
                    ans += 1
            elif c == 0 and r != 0 and r != R-1:
                if field[r-1][c] == "*":
                    ans+=1
                if field[r+1][c] =="*":
                    ans += 1
                if field[r][c+1] =='*':
                    ans+=1
                if field[r+1][c + 1] == '*':
                    ans += 1
                if field[r-1][c + 1] == '*':
                    ans += 1
            elif  r == R-1 and c != 0 and c != C-1:
                if field[r-1][c] == "*":
                    ans += 1
                if field[r][c+1] == "*":
                    ans += 1
                if field[r][c-1] == "*":
                    ans += 1
                if field[r-1][c+1] == "*":
                    ans += 1
                if field[r-1][c-1] == "*":
                    ans += 1

            elif r == R-1 and c == C-1 :
                if field[r-1][c-1] == "*":
                    ans += 1
                if field[r-1][c] == "*":
                    ans += 1
                if field[r][c-1] == "*":
                    ans += 1

            elif c== C-1 and r != 0 and r != R-1:
                if field[r-1][c] == "*":
                    ans += 1
                if field[r-1][c-1] == "*":
                    ans += 1
                if field[r+1][c] == "*":
                    ans += 1
                if field[r+1][c-1] == "*":
                    ans += 1
                if field[r][c - 1] == "*":
                    ans += 1
            
            elif c == C-1 and r == 0:
                if field[r][c-1] == "*":
                    ans += 1
                if field[r+1][c] == "*":
                    ans += 1
                if field[r+1][c-1] == "*":
                    ans += 1
            elif r == 0 and c != 0 and c != C-1:

                if field[r][c+1] == "*":
                    ans += 1
                if field[r][c-1] == "*":
                    ans += 1
                if field[r+1][c] == "*":
                    ans += 1
                if field[r+1][c-1] == "*":
                    ans += 1
                if field[r+1][c+1] == "*":
                    ans += 1
            elif c!=0 and c!=C-1 and r!=0 and r!=R-1  :
                if field[r-1][c-1] == "*":
                    ans += 1
                if field[r-1][c] == "*":
                    ans += 1
                if field[r-1][c+1] == "*":
                    ans += 1
                if field[r][c+1] == "*":
                    ans += 1
                if field[r+1][c+1] == "*":
                    ans += 1
                if field[r+1][c] == "*":
                    ans += 1

                if field[r+1][c-1] == "*":
                    ans += 1
                if field[r][c-1] == "*":
                    ans += 1

            if ans > 0 :
                mat[r][c] = ans
            elif ans == 0 :
                mat[r][c] = "."
        else:
            mat[r][c] = '*'

for i in mat:
    out = "".join(map(str,i))
    print(out)