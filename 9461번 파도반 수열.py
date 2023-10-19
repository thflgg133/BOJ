import sys

dp = [1,1,1,2,2] # P(1) ~ P(5) 

T = int(sys.stdin.readline())

for _ in range(T):
    num = int(sys.stdin.readline())

    if num >= 6: # num이 6 이상일 때에는 dynamic programming을 이용해 구함
        for i in range(5, num):
            dp.append(dp[i-1] + dp[i-5]) # 1~5번째에는 규칙을 찾을 수 없지만 6번째이후 부터는 P(N) = P(N-1) + P(N-5)가 성립함을 알 수 있다
            
        print(dp[num-1])

    else:
        print(dp[num-1])
        
    dp = [1,1,1,2,2] # 다시 초기화