T = int(input())
cnt = 1

for i in range(T):
    H, W, N = map(int, input().split())

    while N > H: # 호수 설정을 위한 코드
        N -= H 
        cnt += 1 

    cnt = str(cnt).zfill(2) # 문자열 앞을 0으로 채워 01 02 03 ... 99 형태로 나타낼 수 있게 만듬
    N = str(N).zfill(2)

    print(int(N + cnt)) # int형으로 형 변환 하면서 zfill로 생성된 숫자앞에 0들 제거
    cnt = 1