a, b, c = map(int, input().split())


if a > b:
  min = b
else:
  min = a

if min > c:
  min = c

print(min)
