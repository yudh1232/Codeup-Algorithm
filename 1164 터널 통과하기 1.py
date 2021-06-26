a, b, c  = map(int, input().split())

if a > b:
  min = b
else:
  min = a

if min > c:
  min = c

if 170 >= min:
  print("CRASH")
else:
  print("PASS")

""" 풀이 2
array = list(map(int, input().split()))

min = min(array)

if 170 >= min:
  print("CRASH")
else:
  print("PASS")
"""
