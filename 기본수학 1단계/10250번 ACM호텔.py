T = int(input())
cnt = 1

for i in range(T):
    H, W, N = map(int, input().split())

    while N > H: # 호수 설정을 위한 코드
        N -= H
        cnt +=1

    cnt = str(cnt).zfill(2) # 두자리를 할당해 01 02 03 ... 99 형태로 나타낼 수 있게 만드는 코드
    N = str(N).zfill(2)
    print(int(N+cnt))
    cnt = 1
