import sys

s = sys.stdin.readline().rstrip().split('-')
ans = 0

for i in s[0].split('+'):
    ans += int(i)

for i in s[1:]:
    for j in i.split('+'):
        ans -= int(j)

print(ans)