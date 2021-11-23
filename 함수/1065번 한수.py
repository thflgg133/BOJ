def solve(N):
    cnt = 0
    for i in range(1,N+1):
        if i < 100:
            cnt +=1
          

        if i > 100:
            nums = list(map(int, str(i)))
            if nums[0] - nums[1] == nums[1] - nums[2]:
               cnt += 1
    print(cnt)

num = int(input())
res = solve(num)
