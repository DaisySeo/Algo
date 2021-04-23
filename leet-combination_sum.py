import sys
input = sys.stdin.readline

def dfs(idx, path, path_sum):
    if path_sum > target:
        return
    elif path_sum == target:
        combination.append(path)
        return
    
    #print('sum: ', path_sum, 'path: ', path, 'comb: ', combination)
    for j in range(idx, len(candidates)):
        dfs(j, path + [candidates[j]], path_sum + candidates[j])

def solution(candidates, target):
    global combination
    combination = []
    path = []

    dfs(0, path, 0)
    
    return combination


candidates = list(input().strip().replace(' ', ''))
for i, num in enumerate(candidates):
    candidates[i] = int(num)
target = int(input())

answer = solution(candidates, target)
print('Answer: ', answer)
