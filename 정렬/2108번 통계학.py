import sys
from collections import Counter
num = []
tmp = {}

for _ in range(int(sys.stdin.readline())):
    num.append(int(sys.stdin.readline()))
num.sort()
print(round(sum(num)/len(num)))
print(num[len(num)//2])
tmp = Counter(num).most_common()
if len(tmp) > 1:
    if tmp[0][1] == tmp[1][1]:
        print(tmp[1][0])

    else:
        print(tmp[0][0])

else:
    print(tmp[0][0])

print(num[-1]-num[0])

# Counter import 안하고 풀어보기