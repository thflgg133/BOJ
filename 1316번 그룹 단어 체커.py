N = int(input())
answer = 0
for i in range(N):
    words = input()
    for j in range(len(words)):
        if j != len(words) -1:
            if words[j] == words[j+1]:
                pass

            elif words[j] in words[j+1:]:
                break

        else:
            answer += 1

print(answer)
