a, b = map(int, input().split())

array = [400, 340, 170, 100, 70]

if array[a - 1] + array[b - 1] > 500:
  print("angry")
else:
  print("no angry")
