K, N = map(int, input().split())
rope = []
ans = 0

for _ in range(K):
    rope.append(int(input())) # [802, 743, 457, 539]

low, high = 0, 10000000000
while low <= high:
    mid = (low + high) // 2
    num = 0
    for i in rope: 
        num = num + (i // mid)
        print(num)
    if num >= N: 
        low = mid + 1
    else: 
        high = mid - 1

print(high)