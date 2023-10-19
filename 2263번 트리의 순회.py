import sys
sys.setrecursionlimit(10**6)

def preorder(inorder_start, inorder_end, postorder_start, postorder_end):
    if inorder_start > inorder_end  or postorder_start > postorder_end:
        return
    
    root = postorder[postorder_end]
    
    print(root, end=" ")
    
    left = position[root] - inorder_start
    right = inorder_end - position[root]
    
    preorder(inorder_start, inorder_start+left-1, postorder_start, postorder_start+left-1)
    preorder(inorder_end-right+1, inorder_end, postorder_end-right, postorder_end-1)


n = int(sys.stdin.readline())
inorder = list(map(int, sys.stdin.readline().split()))
postorder = list(map(int, sys.stdin.readline().split()))
position = [0] * (n+1)
for i in range(n):
    position[inorder[i]] = i
    
preorder(0, n-1, 0, n-1)