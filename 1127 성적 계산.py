ratios = [0] * 3
scores = [0] * 3
result = 0

for i in range(3):
  ratios[i], scores[i] = input().split()
  ratios[i] = float(ratios[i])
  scores[i] = int(scores[i])

for i in range(3):
  result += ratios[i] * scores[i]

print(format(result, ".1f"))
