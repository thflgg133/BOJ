import sys

def paper(x, y, N) :
  color = paper_list[x][y] 
  
  for i in range(x, x+N) :
    for j in range(y, y+N) :
      if color != paper_list[i][j] :  # 같은 색이 아니면 4개의 구역으로 나눔
        paper(x, y, N//2) # 왼쪽 위
        paper(x, y+N//2, N//2) # 오른쪽 위
        paper(x+N//2, y, N//2) # 왼쪽 아래
        paper(x+N//2, y+N//2, N//2) # 오른쪽 아래

        return

  if color == 0 :
    result.append(0)

  else :
    result.append(1)


N = int(sys.stdin.readline())
paper_list = [list(map(int, sys.stdin.readline().split())) for _ in range(N)] 

result = []

paper(0,0,N) # 0,0 부터 탐색 시작

print(result.count(0))
print(result.count(1))