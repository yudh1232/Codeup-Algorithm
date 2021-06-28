n = int(input())
array = list(map(int, input().split()))

sum = 0
for item in array:
  if item % 5 == 0:
    sum += item

print(sum)
