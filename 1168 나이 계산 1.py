a, b = map(int, input().split())
year = a // 10000

if b < 3:
  result = 112 - year + 1
elif b < 5:
  result = 12 - year + 1

print(result)
