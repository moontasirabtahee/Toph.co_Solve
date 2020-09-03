N , M = map(int,input().split())
checker = []

for i in range(M):
    word1,word2 = map(ord,input().split())
    checker.append([word1,word2])

"""minimum = min([min(r) for r in checker])
total = set([x for x in range(65,65+N,1)])
out = set.intersection(*map(set, checker))
"""
