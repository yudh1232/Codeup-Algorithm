h, m = map(int, input().split())

if m < 30:
  m = m + 30
  h = h - 1
  if h == -1:
    h = 23
else:
  m = m - 30

print(h , m)
