import sys

N = int(sys.stdin.readline())
tmp = [0]*10001 # 조건: 수는 10000보다 작거나 같은 자연수, 10001개를 만드는이유? list의 인덱스는 0번 부터 시작하므로

for _ in range(N):
    tmp[int(sys.stdin.readline())] += 1 # 입력받은 수의 빈도 수를 1회 증가시킨다

for i in range(10001):
    if tmp[i] != 0:
        for j in range(tmp[i]): # 수의 인덱스 값 만큼 출력 ex) 예제처럼 1은 2번 입력되었으므로 tmp[1] = 2 이므로 2번출력
           print(i)