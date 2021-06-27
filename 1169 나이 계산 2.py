age = int(input())

if age > 13:
  year = 12 - age + 101
  n = 1
else:
  year = 12 - age + 1
  n = 3

print(year, n)
