import re

#check if palindrome
def check(word):
    word = re.sub('[^a-z0-9]', '', word)
    return word == word[::-1]

def solution(word):
    left, right = 0, 0
    max_word, max_len = '', 0
    while left < len(word):
        for right in range(0, len(word)):
            checked = check( ''.join(word[left:right+1]) )
            if checked == True and (right-left) > max_len:
                max_word = ''.join(word[left:right+1])
                max_len = right - left
            right += 1
        left += 1
        
    return max_word  
            
word = 'babad'

print 'Answer: ', solution(word)
