import sys

def print_star(x, y, N):
    if N == 3:
        star[x][y] = '*'
        star[x+1][y-1] = star[x+1][y+1] = '*'
        
        # 바닥은 전부 별
        for i in range(-2,3):
            star[x+2][y+i] = '*'
            
    else:
        print_star(x, y, N//2)
        print_star(x+N//2, y-N//2, N//2)
        print_star(x+N//2, y+N//2, N//2)


N = int(sys.stdin.readline())
star = [[' '] * 2 * N for _ in range(N)]

print_star(0, N-1, N)
for i in star:
    print("".join(i))