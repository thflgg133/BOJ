# LCS = Longest Common String(최장 공통 부분문자열)
import sys

str1 = list(sys.stdin.readline().rstrip())
str2 = list(sys.stdin.readline().rstrip())
lcs = [[0 for _ in range(len(str2)+1)] for _ in range(len(str1)+1)]

for i in range(1, len(str1)+1):
    for j in range(1, len(str2)+1):
        if str1[i-1] == str2[j-1]:
            lcs[i][j] = lcs[i-1][j-1] + 1

        else:
            lcs[i][j] = max(lcs[i][j-1], lcs[i-1][j])

print(lcs[-1][-1])