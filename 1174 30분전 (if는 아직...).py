h, m = map(int, input().split())

h = (h + (m - 30) // 60) % 24
m = (m - 30) % 60

print(h, m)
