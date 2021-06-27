a, b = map(int, input().split())

if a % b == 0:
  print("{0}*{1}={2}".format(b, int(a / b), a))
elif b % a == 0:
  print("{0}*{1}={2}".format(a, int(b / a), b))
else:
  print("none")
