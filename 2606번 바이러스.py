import sys
from collections import deque

def main():
    computer = {}
    visit = []

    for i in range(int(sys.stdin.readline())):
        computer[i+1] = [] 
               
    for j in range(int(sys.stdin.readline())):
        num1, num2 = map(int, sys.stdin.readline().split())
        computer[num1].append(num2) # 양 방향이므로 입력받은 num1, num2 서로 연결
        computer[num2].append(num1) # 양 방향이므로 입력받은 num2, num1 서로 연결

    queue = deque([1])
    while queue:
        current = queue.popleft()
        
        if current not in visit:
            visit.append(current)
            
            for num in computer[current]:
                queue.append(num)
            
    print(len(visit)-1)

if __name__ == "__main__":
    main()