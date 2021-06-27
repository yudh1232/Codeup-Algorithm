n = int(input())

ten = n // 10
one = n % 10

result = (10 * one + ten) * 2
if result > 100:
  result -= 100

print(result)
if result > 50:
  print("OH MY GOD")
else:
  print("GOOD")
