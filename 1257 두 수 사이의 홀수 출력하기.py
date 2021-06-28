a, b = map(int, input().split())

if a % 2 == 0:
  a += 1

while True:
  if a > b:
    break
  print(a, end = ' ')
  a += 2
