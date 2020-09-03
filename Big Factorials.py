import math
N = int(input())
fact = math.factorial(N)
output = str(fact)[-4:]
print(output)