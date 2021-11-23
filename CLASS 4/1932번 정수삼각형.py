import sys

n = int(sys.stdin.readline())
triangle = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
print(triangle)

if n % 2 == 0:
    total = (1+n) * (n//2)

else: 
    total = ((1+n) * (n//2)) + (n//2 + 1)

triangle = [0] * total
triangle[0] = [triangle[0][0]]

print(triangle)

for i in range(1, len(total)):
    for j in range(2):
        triangle[j]

print(triangle)

