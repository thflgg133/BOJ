def hanoi_tower(n,first,second,third):
    if n == 1:
        print(first,third)

    else:
        hanoi_tower(n-1,first,third,second)
        print(first,third)
        hanoi_tower(n-1,second,first,third)


N = int(input())
print(2**N-1)
hanoi_tower(N,1,2,3)


'''
N = 3 일때
1번에 놓여있는 3이 3번으로 가려면 [1,2]가 2번에 있어야함
[1,2]가 2번 위에 있으려면 그전에 1이 3번 위에 있어야함

N = 4 일때
1번에 놓여있는 4가 3번으로 가려면 [1,2,3]이 2번에 있어야함
[1,2,3]이 2번 위에 있으려면 그전에 [1,2]가 3번 위에 있어야함
[1,2]가 3번 위에 있으려면 그전에 1이 2번 위에 있어야함

...

즉 N이 홀수 일때 1은 3번으로 먼져 가야함 5
(N-1)개를 2번으로 옮김 4
(N-1-1)개를 3번으로 옮김 3
(N-1-1-1)개를 2번으로 옮김 2
(N-1-1-1-1)개를 3번으로 옮김 1

N이 짝수 이면 1은 2번으로 먼져 가야함

'''
