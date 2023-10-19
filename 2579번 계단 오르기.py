import sys

stair = int(sys.stdin.readline())

# 계단의 개수는 최대 300 이므로 0번째 인덱스를 고려하여 0 ~ 300 까지 301개 생성
score = [0]*301
dp = [0]*301

for i in range(1, stair+1):  
    score[i] = int(sys.stdin.readline())
    
dp[1] = score[1] # 처음 1칸 올라가는 경우
dp[2] = score[1] + score[2] # 처음 2칸 올라가는 경우 
dp[3] = max(score[1] + score[3], score[2] + score[3]) # 연속된 세칸을 밟으면 안되므로 (1칸 올라간후 2칸 올라가거나) or (2칸 올라간 후 1칸 올라가거나)
                                                      # 둘 중 더 높은 점수를 얻을 수 있는 방법으로 올라간다

for i in range(4, stair+1): # 마지막 칸은 무조건 밟아야하고 연속된 세칸을 밟으면 안되므로 두 가지 방법 중 더 높은 점수를 얻을 수 있는 방법을 선택  
    dp[i] = max(score[i] + score[i-1] + dp[i-3], score[i]+ dp[i-2])

print(dp[stair])