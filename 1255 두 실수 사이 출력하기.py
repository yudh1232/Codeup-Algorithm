f1, f2 = map(float, input().split())

while True:
  print(format(f1, ".2f"), end = ' ')
  f1 += 0.01
  if f1 > f2:
    break
