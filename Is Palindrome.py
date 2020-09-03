word = input()
count = 0
for first,last in zip(word,reversed(word)):
    if first == last:
        count += 1
    else:
        print('No')
        break

if count == len(word):
    print("Yes")