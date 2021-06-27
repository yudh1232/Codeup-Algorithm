a, b, c = map(int, input().split())

if a > b:
  max = a
  min = b
else:
  max = b
  min = a

if max < c:
  result = max
else:
  if min < c:
    result = c
  else:
    result = min

print(result)
