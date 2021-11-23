'''
N = int(input())
tmp = []

for _ in range(N):
    word = input()
    tmp.append((len(word), word))

new_list = list(set(tmp))
new_list.sort()
for i in range(len(new_list)):
    print(new_list[i][1])

'''
words_num = int(input())
words_list = []

for _ in range(words_num):
    word = input()
    word_count = len(word)
    words_list.append((word_count, word))


#중복 삭제
words_list = list(set(words_list))
print(words_list)
#단어 숫자 정렬 > 단어 알파벳 정렬
words_list.sort(key = lambda word: (word[0], word[1]))
print(words_list)
for word in words_list:
    print(word[1])
