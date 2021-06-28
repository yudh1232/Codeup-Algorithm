array = list(map(int, input().split()))
i = 0

while True:
  if i > 9:
    break
  if array[i] % 5 == 0:
    print(array[i])
    break
  i += 1

if i == 10:
  print(0)
