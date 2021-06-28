c1, c2 = input().split()
n1, n2 = ord(c1), ord(c2)

while True:
  print(chr(n1), end = ' ')
  n1 += 1
  if n1 > n2:
     break
