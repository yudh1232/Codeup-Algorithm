height, weight = map(float, input().split())

standard_weight = (height - 100) * 0.9
obesity = (weight - standard_weight) * 100 / standard_weight

if obesity > 20:
  print("비만")
elif obesity > 10:
  print("과체중")
else:
  print("정상")
