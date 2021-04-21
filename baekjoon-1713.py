import collections
import sys

def check_least(mark, counter, pic):
    new_counter = dict()
    for item in pic:
        new_counter[item] = counter[item]
        
    least = min(new_counter.values())
    if counter[mark] == least:
        return True
    else:
        return False

def solution(pic_num, stu_num, rec):
    pic, idx = [0, 0, 0], [0, 0, 0]
    counter = collections.defaultdict(int)
    
    for i in range(0, stu_num):
        counter[rec[i]] += 1

        for j in range(0, pic_num):
            if 0 in pic:
                if pic[j] == 0:
                    pic[j] = rec[i]
                    idx[j] = i
                    break
            elif i in pic:
                break
            else:
                oldest = min(idx)
                checked = check_least(pic[j], counter, pic)
                if idx[j] == oldest and checked == True:
                    counter[pic[j]] = 0
                    pic[j] = rec[i]
                    idx[j] = i
                    break
    return pic

input = sys.stdin.readline
pic_num = int(input())
stu_num = int(input())
rec = list(map(int, input().split(" ")))

answer = solution(pic_num, stu_num, rec)
answer = sorted(answer)
print(answer)
