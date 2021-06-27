lotto_number = list(map(int, input().split()))
bonus_number = lotto_number.pop()
my_number = list(map(int, input().split()))

count = 0
bonus = 0

for i in range(len(my_number)):
  if my_number[i] in lotto_number:
    count += 1
  elif my_number[i] == bonus_number:
    bonus += 1

if count == 6:
  print(1)
elif count == 5:
  if bonus == 1:
    print(2)
  elif bonus == 0:
    print(3)
elif count == 4:
  print(4)
elif count == 3:
  print(5)
elif count <= 2:
  print(0)
