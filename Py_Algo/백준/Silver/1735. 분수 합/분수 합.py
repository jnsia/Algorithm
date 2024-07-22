import sys
import math

input = sys.stdin.readline

a, b = map(int, input().split())
c, d = map(int, input().split())

gcm_num1 = math.gcd(b, d)

f = (b * d) // gcm_num1
e = a * (d // gcm_num1) + c * (b // gcm_num1)

gcm_num2 = math.gcd(e, f)

if gcm_num2 != 1:
    e = e // gcm_num2
    f = f // gcm_num2

print(e, f)