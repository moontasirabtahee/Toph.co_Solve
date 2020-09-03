s =int(input())
text = input()
result = ''

for i in range(len(text)):
    char = text[i]

    # Encrypt uppercase characters
    if (char.isupper()):
        result += chr((ord(char) - s - 65) % 26 + 65)

        # Encrypt lowercase characters
    elif (char.islower()):
        result += chr((ord(char) - s - 97) % 26 + 97)
    else:
        result += char
print(result)