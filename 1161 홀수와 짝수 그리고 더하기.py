a, b = map(int, input().split())

if a % 2 == 1:
  s1 = "홀수"
else:
  s1 = "짝수"

if b % 2 == 1:
  s2 = "홀수"
else:
  s2 = "짝수"

if (a + b) % 2 == 1:
  s3 = "홀수"
else:
  s3 = '짝수'

print("{0}+{1}={2}".format(s1, s2, s3))
