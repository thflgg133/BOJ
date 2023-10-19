
import sys

words_list = set() #중복된 단어는 삭제하기 위해 set으로 할당

for _ in range(int(sys.stdin.readline())):
    words_list.add(sys.stdin.readline().rstrip()) # set은 list와 다르게 append() 함수 대신 add() 함수 사용, rstrip을 통해 문자열 뒤 \n 붙는 것 방지

words_list = list(words_list) # sort 함수 사용을 위해 리스트 화

# 알파벳 순서로 정렬 -> 알파벳 순서로 정렬된 리스트를 다시 짧은 단어 순으로 정렬
# Why? 길이로만 비교하면 단어의 알파벳 순서로 정렬되지 않으니까
words_list.sort() 
words_list.sort(key = lambda word: len(word))

print("\n".join(words_list)) # 줄 바꿈 \n 과 join 함수를 통해 각 줄당 단어 하나씩 출력