N = input().title()
string =''

for i in N:

    if i == 's':
        string+='$'
    elif i == "i":
        string+="!"
    elif i=='o':
        string+="()"
    else:
        string+=i

string=string+"."

print(string)
