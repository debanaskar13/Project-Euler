import sys

t = int(input().strip())
for a0 in range(t):
    m = -1
    n = int(input().strip())
    for a in range(3, (n // 3) + 1):
        b = (n**2 - 2 * a * n) // (2 * n - 2 * a)
        c = n - a - b
        if a**2 + b**2 == c**2 and a + b + c == n:
            if a * b * c > m:
                m = a * b * c
    print(m)