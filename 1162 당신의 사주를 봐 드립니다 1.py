a, b, c  = map(int, input().split())

result = a - b + c

if result % 10 == 0:
  print("대박")
else:
  print("그럭저럭")
