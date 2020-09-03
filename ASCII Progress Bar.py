n = float(input())
pluscount = int(n//10)
num = int(n)
plus = ['+']*pluscount
dot = ['.']*(10-pluscount)
plus = plus+dot
plus = ''.join(plus)
string = f"[{plus}] {num}%"
print(string)
