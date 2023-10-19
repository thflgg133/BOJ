import sys
sys.setrecursionlimit(10**6)

def dfs(num):
    global ans

    # 선택된 학생은 방문처리를 하고 사이클에 추가한다
    choose = students[num-1]
    visited[num] = True
    cycle.append(num)

    # 선택된 학생이 이미 조를 형성했는지, 이번에 조를 형성하는지 판단
    if visited[choose]:
        # 이번에 조를 형성할 때
        if choose in cycle:
            # 조 사이클이 형성된 학생들만 ans에 추가함
            ans += cycle[cycle.index(choose):]

        return

    # 아직 방문처리가 되지 않았으므로 다시 dfs문 실행
    else:
        dfs(choose)

    # 조를 형성하지 못한 경우
    return


T = int(sys.stdin.readline())

for _ in range(T):
    n = int(sys.stdin.readline())
    visited = [False] * (n+1)
    students = list(map(int, sys.stdin.readline().split()))
    ans = []

    for i in range(1, n+1):
        # 이미 조를 편성한 학생은 탐색할 필요 없음
        if not visited[i]:
            cycle = []
            dfs(i)

    print(n - len(ans))