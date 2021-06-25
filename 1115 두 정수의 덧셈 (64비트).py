# 파이썬 3에서는 long 타입이 없어지고 int 타입만 남았는데, 이 int가 arbitrary precision을 지원하여 오버플로우가 발생하지 않게 되었다.

a, b = map(int, input().split())
print(a + b)
