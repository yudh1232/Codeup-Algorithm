array = []

for _ in range(19):
  array.append(list(map(int, input().split())))

n = int(input())

for _ in range(n):
  x, y = map(int, input().split())
  for i in range(19):
    if array[x - 1][i] == 0:
      array[x - 1][i] = 1
    else:
      array[x - 1][i] = 0

    if array[i][y - 1] == 0:
      array[i][y - 1] = 1
    else:
      array[i][y - 1] = 0

for i in range(19):
  for j in range(19):
    print(array[i][j], end = ' ')
  print()
