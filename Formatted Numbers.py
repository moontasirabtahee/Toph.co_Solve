N = input()
count = 0
parts = []
tut = ""
pointer = 0
for i in reversed(N):

    tut = tut + i
    count+=1
    if count==3:
        parts.append(tut)
        tut = ""
        count=0
    if pointer == len(N)-1  and count != 3 and count != 0:

        parts.append(tut)

    pointer+=1
parts =  [x[::-1] for x in parts]
output = ",".join((parts[::-1]))

print(output)

