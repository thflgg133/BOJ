import sys
sys.setrecursionlimit(10 ** 6) # python에서는 재귀 깊이 제한은 1000으로 걸려있기 때문에 인위적으로 늘려줘야 한다

def postorder(start, end):
    if start > end:
        return

    root = preorder[start] # 시작 노드
    idx = start + 1
    
    for i in range(idx, end+1):  
        if preorder[i] > root: # 서브 노드가 뿌리 노드보다 크다면 # 인덱스 재설정
            idx = i # Why? 값이 역전되는 순간 왼쪽 으로 들어가지 않았다는 뜻이기 때문 => 오른쪽 노드로 방향이 바뀌었다는 뜻
            break

    postorder(start+1, idx-1) # 왼쪽 서브 트리
    postorder(idx, end) # 오른쪽 서브 트리
    print(root) # 루트


preorder = []
while True: # 입력이 따로 주어지지 않았기 때문에 try except문을 사용하여 입력한다 

    try:
        preorder.append(int(sys.stdin.readline()))

    except:
        break

postorder(0, len(preorder)-1)