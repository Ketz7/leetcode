import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        string = s 
        pattern = re.compile('[\W_]+')
        x = pattern.sub('', string.lower())
        y = len(x) - 1 
        for z in range(len(x)):
            start = x[z]
            end = x[y]
            y -= 1
            if start != end:
                return False
        return True