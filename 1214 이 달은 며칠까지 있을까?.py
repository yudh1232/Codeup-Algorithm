y, m = map(int, input().split())

if m in [1, 3, 5, 7, 8, 10, 12]:
  print(31)
elif m != 2:
  print(30)
elif m == 2:
  if ((y % 4 == 0) and (y % 100 !=0)) or (y % 400 == 0):
    print(29)
  else:
    print(28)
