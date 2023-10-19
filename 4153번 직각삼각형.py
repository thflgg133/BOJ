while True:
    num = list(map(int, input().split()))
    if num[0] == num[1] == num[2] == 0:
        break
    else:
        num.sort()
    
    if num[0] ** 2 + num[1] ** 2 == num[2] ** 2:
        print("right")

    else:
        print("wrong")