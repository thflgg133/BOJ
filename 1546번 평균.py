N = int(input())
score = list(map(int, input().split()))
M = max(score)
answer = 0
answer += (sum(score)/M*100)/len(score)
print(answer)