import sys
input = sys.stdin.readline

def dfs(idx, word):
    if len(word) == len(num):
        combination.append(word)
        return
    
    for i in range(idx, len(num)):
        for char in keyboard[int(num[i])]:
            dfs(i + 1, word + char)

def solution(num):
    global combination, keyboard
    keyboard = {1: '', 2: 'abc', 3: 'def', 4: 'ghi', 5: 'jkl', 6: 'mng', 7: 'pqrs', 8: 'tuv', 9: 'wxyz', 0: '+'}
    combination = []
    word = ""

    dfs(0, word)

    return combination


num = input().strip('\n')

answer = solution(num)
print('Answer: ', answer)
