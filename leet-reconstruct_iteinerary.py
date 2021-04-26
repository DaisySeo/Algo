import collections
import sys
input = sys.stdin.readline
    
def solution(from_to, cnt):
    path = ['JFK']

    fr = 'JFK'
    for i in range(0, cnt):
        temp = fr
        fr = from_to[fr][0]
        del from_to[temp][0]
        path.append(fr)
    
    return path


travel = input().split()
from_to = collections.defaultdict(list)
cnt = 0
for i, airport in enumerate(travel):
    airport = airport.strip("[],‘’")
    travel[i] = airport
    if i%2 != 0:
        from_to[travel[i-1]].append(travel[i])
        from_to[travel[i-1]] = sorted(from_to[travel[i-1]])
        cnt += 1

print(from_to)
answer = solution(from_to, cnt)
print('Answer: ', answer)
