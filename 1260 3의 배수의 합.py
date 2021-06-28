a, b = map(int, input().split())
sum = 0

if a % 3 == 1:
  a += 2
elif a % 3 == 2:
  a += 1

while True:
  if a > b:
    break
  sum += a
  a += 3

print(sum)
