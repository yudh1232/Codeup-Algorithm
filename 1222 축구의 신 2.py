t, a, b = map(int, input().split())

while True:
  if t >= 90:
    break
  a += 1
  t += 5

if a > b:
  print("win")
elif a < b:
  print("lose")
else:
  print("same")
