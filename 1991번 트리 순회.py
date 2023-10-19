import sys

def preorder(root): # 전위 순위
    if root != '.':
        print(root, end="")     # 루트
        preorder(tree[root][0]) # 왼쪽
        preorder(tree[root][1]) # 오른쪽


def inorder(root): # 중위 순위
    if root != '.':
        inorder(tree[root][0]) # 왼쪽
        print(root, end="")    # 루트
        inorder(tree[root][1]) # 오른쪽


def postorder(root): #후위 순위
    if root != '.':
        postorder(tree[root][0]) # 왼쪽
        postorder(tree[root][1]) # 오른쪽
        print(root, end="")      # 루트


N = int(sys.stdin.readline())
tree = {} # dictionary로 설정해서 트리형태로 만듬

for _ in range(N):
    root, left, rigth = sys.stdin.readline().rstrip().split()
    tree[root] = [left, rigth] # 각 root 에 좌측, 우측 뿌리 노드 설정

preorder('A')
print()
inorder('A')
print()
postorder('A')