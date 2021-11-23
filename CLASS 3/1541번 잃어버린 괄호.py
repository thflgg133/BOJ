import sys

s = sys.stdin.readline().rstrip().split('-') # -를 기준으로 나눠서 리스트화
ans = 0

 # -를 기준으로 안나눠진다는 것은 + 식이므로 +를 기준으로 나눠서 더해줌
for i in s[0].split('+'): 
    ans += int(i)

for i in s[1:]: 
    for j in i.split('+'):
        ans -= int(j)

print(ans)