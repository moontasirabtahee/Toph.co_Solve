R,C = map(int,input().split())
matrix = []
for i in range(R):
    temp = input()
    matrix.append([charecter for charecter in temp])

output = 0
for r in range(R):
    for c in range(C):
        if matrix[r][c] == "*":
            continue
        else :
            if r == 0 and c != 0 and c!=C-1 :
                if matrix[r][c-1] == '.' and matrix[r][c+1]=="." and matrix[r+1][c]=='.':
                    output += 1
            elif r == 0 and c==0:
                if matrix[r][c+1] == '.' and matrix[r+1][c]=='.':
                    output+=1
            elif r == 0 and c == C-1:
                if matrix[r][c-1]=='.' and matrix[r+1][c]=='.':
                    output+=1
            elif c == 0 and r ==R-1:
                if matrix[r-1][c]=='.' and matrix[r][c+1]=='.':
                    output+=1
            elif c == 0 and r !=0 and r != R-1:
                if matrix[r+1][c]=='.' and matrix[r-1][c] == '.'and matrix[r][c+1]=='.':
                    output +=1
            elif r == R-1 and c == C-1:
                if matrix[r-1][c] == '.' and matrix[r][c-1]=='.':
                    output+=1
            elif r==R-1 and c != 0 and c!=C-1:
                if matrix[r][c+1] == '.' and matrix[r][c-1] == '.' and matrix[r-1][c]=='.':
                    output+=1
            elif c==C-1 and r != 0 and r != R-1:
                if matrix[r+1][c]=='.' and matrix[r-1][c]=='.' and matrix[r][c-1]==".":
                    output+=1
            else:
            #elif c > 0 and c<C-1 and r>0 and r<R-1:
                if matrix[r][c+1]=='.' and matrix[r][c-1] =='.' and matrix[r+1][c]=='.' and matrix[r-1][c]==".":
                    output+=1
print(output)