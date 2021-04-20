import itertools

def check(candidates, banned_id):
    match = 0
    for idx, banned in enumerate(banned_id):
        if len(candidates[idx]) != len(banned):
            return False
        else:
            for i in range(0, len(candidates[idx])):
                if candidates[idx][i] != banned[i] and banned[i] != '*':
                    return False
    return True

def solution(user_id, banned_id):
    
    candidates = list(itertools.permutations(user_id, len(banned_id)))
    
    mark = 0
    matched = []
    
    for candidate in candidates:
        mark = check(candidate, banned_id)
        candidate = set(candidate)
        if mark == True and candidate not in matched:
            matched.append(candidate)
                
    answer = len(matched)
    return answer
