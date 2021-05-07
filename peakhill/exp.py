import binascii
import os
import pickle

data1_ascii = ""
with open('.creds', 'r') as f1:
    data1 = f1.read()
    data1 = int(data1, 2)
    data1_ascii = binascii.unhexlify('%x' % data1)

with open('data', 'wb') as f2:
    f2.write(data1_ascii)

mm1 = []
mm2 = []
cnt1 = 0
cnt2 = 0

with open('data', 'rb') as f3:
    act = pickle.load(f3)
    for j in act:
        if "ssh_user" in j[0]:
            mm1.append(((int)(j[0].replace("ssh_user","")), j[1]))
            cnt1 += 1
        elif "ssh_pass" in j[0]:
            mm2.append(((int)(j[0].replace("ssh_pass","")), j[1]))
            cnt2 += 1

mm1.sort()
mm2.sort()

print("Username: ")
[print(j[1],end="") for j in mm1]
print()
print("password: ")
[print(j[1],end="") for j in mm2]
print()