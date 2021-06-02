dec=[]
with open('rsa','r') as ff:
  arr = ff.readlines()
  # ff[0] => that string
  # ff[1] => rs akey
  ll = arr[1].strip().split(" ")
  for j in ll:
    dec.append(int(j)**61527%37627)

for j in dec:
  print(chr(j),end="")