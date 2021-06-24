n = int(input())
a = list(map(int, input().split()))

min = 9999

for i in range(n):
  if a[i] < min:
    min = a[i]

print(min)
