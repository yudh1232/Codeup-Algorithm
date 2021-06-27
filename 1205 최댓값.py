a, b = map(float, input().split())

array = []
array.append(a + b)
array.append(a - b)
array.append(b - a)
array.append(a * b)
array.append(a / b)
array.append(b / a)
array.append(a ** b)
array.append(b ** a)

print(format(max(array), ".6f"))
