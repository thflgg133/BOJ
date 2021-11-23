import sys

def quad_tree(x,y,N):
    point = tree[x][y]

    for i in range(x,x+N):
        for j in range(y,y+N):
            if point != tree[i][j]:
                answer.append("(")
                quad_tree(x,y,N//2)
                quad_tree(x,y+N//2,N//2)
                quad_tree(x+N//2,y,N//2)
                quad_tree(x+N//2,y+N//2,N//2)
                answer.append(")")

                return answer
                
    if point == '1':
        answer.append('1')   
             
    if point == '0':
        answer.append('0')        

    return answer


N = int(sys.stdin.readline())

tree = [sys.stdin.readline().rstrip() for _ in range(N)]
answer = []

print(''.join(quad_tree(0,0,N)))