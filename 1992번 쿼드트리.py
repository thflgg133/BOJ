import sys

def quad_tree(x,y,N):
    point = tree[x][y]

    for i in range(x,x+N):
        for j in range(y,y+N):
            if point != tree[i][j]: # 같은 색의 점이 아니면 분활
                answer.append("(") # 분할될 떄 마다 괄호 추가
                quad_tree(x,y,N//2) # 2 사분면
                quad_tree(x,y+N//2,N//2) # 3 사분면
                quad_tree(x+N//2,y,N//2) # 1 사분면
                quad_tree(x+N//2,y+N//2,N//2) # 4 사분면
                answer.append(")") # 분할될 떄 마다 괄호 추가

                return answer
                
    if point == '1':
        answer.append('1')   
             
    if point == '0':
        answer.append('0')        

    return answer


N = int(sys.stdin.readline())
tree = [sys.stdin.readline().rstrip() for _ in range(N)]
answer = []

print(''.join(quad_tree(0,0,N))) # 좌표 0,0 부터 순차적으로 탐색