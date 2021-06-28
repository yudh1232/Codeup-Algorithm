n = int(input())
array = list(map(int, input().split()))

count = 0
for item in array:
  if item % 2 == 0:
    count += 1

print(count)
