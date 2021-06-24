array = []
for _ in range(10):
  array.append(list(map(int, input().split())))

# 개미집 (2, 2)
i = 1
j = 1

array[i][j] = 9 # 개미집 방문

# 오른쪽과 아래쪽이 아래가 벽이 아닐 때까지
while True:
  # 오른쪽이 벽이 아닐 때
  if array[i][j + 1] != 1:
    j += 1
    if array[i][j] == 2:
      array[i][j] = 9
      break
    array[i][j] = 9
  
  # 오른쪽이 벽이면서 아래쪽이 벽이 아닐 때
  elif array[i + 1][j] != 1:
    i += 1
    if array[i][j] == 2:
      array[i][j] = 9
      break
    array[i][j] = 9
  
  # 오른쪽과 아래쪽 모두 벽일 때
  else:
    break

# 답 출력
for i in range(10):
  for j in range(10):
    print(array[i][j], end = ' ')
  print()
