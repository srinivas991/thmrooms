s="/bin/bash"

print()

for j in s:
    num=ord(j)
    b=bin(num)
    bb=str(b)
    x=bb[2:]
    while len(x) < 8:
        x='0'+x
    print(x,end=" ")