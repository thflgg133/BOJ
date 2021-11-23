C = int(input())
avg = 0

for i in range(C):
    case = list(map(int, input().split()))
    avg = sum(case[1:]) / case[0]  # 평균을 구함 (nums[0]: 학생수, nums[1:] 점수)
    count = 0
    for j in case[1:]:
        if j > avg:
            count += 1  # 평균 이상인 학생 수
    rate = count/case[0] *100
    print("%.3f"%round(rate,3)+"%")