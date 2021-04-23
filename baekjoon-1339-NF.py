import collections
import sys
input = sys.stdin.readline

def compare(counter, words, i, j):
    padding = len(words[i-1]) - len(words[i]) + j
    print(words[i-1][padding], words[i][j], ' :: ', counter[words[i-1][padding]], counter[words[i][j]])
    if counter[words[i-1][padding]] >= counter[words[i][j]]:
        num[words[i][j]] = num[words[i-1][padding]] - 1
        for cnt in range(padding + 1, len(words[i-1])):
            num[words[i-1][cnt]] -= 1
    else:
        num[words[i][j]] = num[words[i-1][padding]]
        for cnt in range(padding, len(words[i-1])):
            num[words[i-1][cnt]] -= 1

def sumWord(word):
    sum = 0
    for idx, char in enumerate(word):
        sum += (10**(len(word)-idx-1)) * num[char]
    print(word, ': ', sum)
    return sum

def solution(N, new_list):
    cur_num = 9 
    global num
    num = dict()
    
    new_list = sorted(new_list, key=len, reverse=True)
    print(new_list)
    for idx in range(0, N):
        for char_idx, char in enumerate(new_list[idx]):
            if idx == 0:
                if char not in num:
                    num[char] = cur_num
                    cur_num -= 1
            else:
                if char not in num:
                    compare(counter, new_list, idx, char_idx)
        print('num; ', num)

    #print('num: ', num)
    total = 0
    for word in words:
        total += sumWord(word)
    
    return total


N = int(input())
words = []
new_list = []
counter = collections.defaultdict(int)

for i in range(0, N):
    checked = []
    word = input().strip('\n')
    words.append(word)
    for char in word:
        counter[char] += 1
        if char not in checked:
            checked.append(char)
    new_list.append(''.join(checked))

answer = solution(N, new_list)
print('Answer: ', answer)
