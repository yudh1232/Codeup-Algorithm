n = int(input())
a = list(map(int, input().split()))

answer = [0] * 23

for i in range(n):
  answer[a[i] - 1] += 1

for i in range(23):
  print(answer[i], end = ' ')
