# Greedy Algorithm
A, B = map(int, input().split())
cnt = 1
while True:

	# A와 B가 같아질 때 종료
    if A == B:
        break

	# a를 2로 나눈 나머지가 0이 아니고 10으로 나눈 나머지가 1이 아니거나, b가 a보다 작은 경우
    elif (B % 2 != 0 and B % 10 != 1) or (B < A):
        cnt = -1
        break
    
    else:
    	# 10으로 나누었을 때 나머지가 1인 경우
        if B % 10 == 1:
            B //= 10
            cnt += 1
        
        # 2로 나누었을 때 나머지가 0인 경우
        else:
            B //= 2
            cnt += 1

print(cnt)