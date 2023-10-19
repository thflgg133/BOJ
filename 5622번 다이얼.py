words = input()
word_list = ['ABC','DEF','GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
answer = 0

for word in words:
    for _ in word_list:
        if(word in _ ):
            answer += word_list.index(_) +3

print(answer)
