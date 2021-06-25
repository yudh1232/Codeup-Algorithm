s = input()

# len(s)
for i in range(len(s)):
  if s[i] == 'H':
    H_index = i
    break

C = int(s[1 : H_index])
H = int(s[H_index + 1: len(s)])

print(C * 12 + H)
