N = int(input())
binary = bin(N)

setbits = [ones for ones in binary[2:] if ones=='1']
setbits = int(''.join(setbits),2)
print(setbits)