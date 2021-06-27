n = int(input())

if n > 10 and n <= 20:
  print("{0}th".format(n))
elif n % 10 == 1:
  print("{0}st".format(n))
elif n % 10 == 2:
  print("{0}nd".format(n))
elif n % 10 == 3:
  print("{0}rd".format(n))
else:
  print("{0}th".format(n))
