a, b = map(int, input().split())

if a > b:
  while True:
    print(b, end = ' ')
    b += 1
    if a < b:
      break
elif a < b:
  while True:
    print(a, end = ' ')
    a += 1
    if a > b:
      break
else:
  print(a)
