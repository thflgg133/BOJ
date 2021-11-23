T = int(input())

for _ in range(T):
    x, y = map(int , input().split())
    
    distance = y - x
    cnt = 0
    diff = int(distance ** 0.5) # 8일떄 2
    print(diff)
    diff_square = diff ** 2
    print(diff_square)
    if distance < 4: # distance가 1,2,3, 일 떄 규칙에서 예외이므로 그대로 distance값 출력
        cnt = distance

    elif distance > diff_square + diff: # distance 가 distance의 제곱 + distance의 제곱근 일때, diff_square 대신 distance를 안쓰는 이유 : 0.5제곱을 한 이후 int선언을 하면 내림으로 처리되기 떄문에 값이 달라질 수 있으므로 안됨
        cnt = 2 * diff + 1
        
    elif distance > diff_square and distance <= diff_square + diff:
        cnt = 2 * diff

    elif distance == diff_square:
        cnt = 2 * diff -1

    print(cnt)


'''
규칙 제곱근을 한계로 제곱 + 제곱근 형태 이후로 cnt += 1

1   1                   cnt = 1
2   11                  cnt = 2     1,2,3 일때는 예외 distance 값 그대로 cnt 에 할당됨
3   111                 cnt = 3     
4   121     (2^2)       cnt = 3   
5   1211                cnt = 4     
6   1221    (2^2 + 2)   cnt = 4     
7   12211               cnt = 5
8   12221               cnt = 5
9   12321   (3^2)       cnt = 5
10  123211              cnt = 6     
11  123221              cnt = 6 
12  123321              cnt = 6
13  1233211 (3^2 + 3)   cnt = 6
14                      cnt = 7 
'''
