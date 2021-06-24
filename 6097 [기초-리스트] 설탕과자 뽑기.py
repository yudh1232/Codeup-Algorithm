h, w = map(int, input().split())

array = [[0] * w for _ in range(h)]

n = int(input())

for _ in range(n):
  l, d, x, y = map(int, input().split())
  for i in range(l):
    if d == 0:
      array[x - 1][y - 1 + i] = 1
    if d == 1:
      array[x - 1 + i][y - 1] = 1

for i in range(h):
  for j in range(w):
    print(array[i][j], end = ' ')
  print()
