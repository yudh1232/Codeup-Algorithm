array = list(map(int, input().split()))

for i in range(len(array) - 1):
  for j in range(len(array) - 1 - i):
    if array[j] > array[j + 1]:
      array[j], array[j + 1] = array[j + 1], array[j]

for i in array:
  print(i, end = ' ')
