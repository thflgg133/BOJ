import sys

str1 = list(sys.stdin.readline().rstrip())
str2 = list(sys.stdin.readline().rstrip())
# 행은 첫번째 문자열, 열은 두번째 문자열
lcs = [["" for _ in range(len(str2)+1)] for _ in range(len(str1)+1)]

for i in range(1,len(str1)+1):
    for j in range(1,len(str2)+1):

        # 가장 긴 부분수열 최신화
        if str1[i-1] == str2[j-1]:
            lcs[i][j] = lcs[i-1][j-1] + str1[i-1]
        
        # 지금까지의 가장 긴 부분수열을 유지시켜줌으로써 갱신될 수 있도록 만듬
        else:
            if len(lcs[i-1][j]) > len(lcs[i][j-1]):
                lcs[i][j] = lcs[i-1][j]
                
            else:
                lcs[i][j] = lcs[i][j-1]
            
print(len(lcs[-1][-1]))
print(lcs[-1][-1])