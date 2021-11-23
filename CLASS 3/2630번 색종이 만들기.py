import sys

def paper(x, y, N) :
  color = paper_list[x][y]
  for i in range(x, x+N) :
    for j in range(y, y+N) :
      if color != paper_list[i][j] :  # i = 1, j = 0
        paper(x, y, N//2)
        paper(x, y+N//2, N//2) 
        paper(x+N//2, y, N//2)
        paper(x+N//2, y+N//2, N//2)

        return

  if color == 0 :
    result.append(0)

  else :
    result.append(1)


N = int(sys.stdin.readline())
paper_list = [list(map(int, sys.stdin.readline().split())) for _ in range(N)] 

result = []

paper(0,0,N)

print(result.count(0))
print(result.count(1))