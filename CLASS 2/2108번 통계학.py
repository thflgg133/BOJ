import sys
from collections import Counter

num = [int(sys.stdin.readline()) for _ in range(int(sys.stdin.readline()))]
tmp = {}
num.sort()

print(round(sum(num)/len(num))) # 산술평균 소수점 이하 첫째 자리에서 반올림한 값 round()함수를 이용
print(num[len(num)//2])

tmp = Counter(num).most_common() # Counter(data).most_common() 데이터의 개수가 많은 순으로 정렬 해줌
if len(tmp) > 1: 
    if tmp[0][1] == tmp[1][1]: # 최빈값이 있을 때 최빈값 중 두번째로 작은 값 출력 
        print(tmp[1][0])

    else:
        print(tmp[0][0])

else:
    print(tmp[0][0])

print(num[-1]-num[0]) # 범위는 가장 큰 값에서 작은 값을 뺀 것