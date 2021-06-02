# ky + 2367 = 45^x
# y is a product of two prime numbers

sample = "BEGIN"
samplearr = [9709, 8600, 28638, 18410, 1735]

primes = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,51,53,59,61,67,71,73,79,83,89,91,97]

def compareList(l1,l2):
   l1.sort()
   l2.sort()
   if(l1==l2):
      return "Equal"
   else:
      return "Non equal"

def gcd(a, b):
  if b == 0:
    return a
  return gcd(b, a%b)

def printencrypted(i, mult):
  exparr = []
  for j in sample:
    ascval = ord(j)
    expval = (ascval**i)%mult
    exparr.append(expval)
  compareList(exparr, samplearr)

def func(mult, phi):
  for i in range(2, phi):
    if gcd(i,mult) == 1 and gcd(i,phi) == 1:
      # this is a possible key
      printencrypted(i, mult)

for j in primes:
  for k in primes:
    mult = j*k
    phi = (j-1)*(k-1)
    func(mult, phi)