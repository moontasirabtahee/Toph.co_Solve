import statistics 
from statistics import mode

N = input()
aList =list(map(int, str(N)))
print(mode(aList))