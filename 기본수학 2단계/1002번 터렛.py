T = int(input())

for _ in range(T):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    distance = ((x1-x2) ** 2 + (y1-y2) ** 2) ** (1/2)
    if distance == r1 + r2 or distance == abs(r1 - r2):
        print(1)
    
    elif abs(r1 - r2) < distance < (r1 + r2):
        print(2)

    elif distance == 0 and r1 == r2:
        print(-1)

    else:
        print(0)

# 두 원이 일치할때 -1
# 두 원이 내접 외접할때 1
# 두 원이 만나지 않을 때, 한 원이 다른원 내부에 있을 때 0
# 두 원이 두 점에서 만날때 2