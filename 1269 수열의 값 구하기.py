a, b, c, n = map(int, input().split())

for _ in range(n - 1):
  a = a * b + c

print(a)
