t, a = map(int, input().split())

while True:
  if t < 90:
    a += 1
    t += 5
  else:
    break

print(a)
