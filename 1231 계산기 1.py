s = input()

for i in range(len(s)):
  if s[i] == '+':
    a, b = map(int, s.split('+'))
    print(a + b)
    break
  elif s[i] == '-':
    a, b = map(int, s.split('-'))
    print(a - b)
    break
  elif s[i] == '*':
    a, b = map(int, s.split('*'))
    print(a * b)
    break
  elif s[i] == '/':
    a, b = map(int, s.split('/'))
    print(format(a / b, ".2f"))
    break
