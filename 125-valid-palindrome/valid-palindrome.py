# import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        # pattern = re.compile('[\W_]+')
        # x = pattern.sub('', s.lower())
        # y = len(x) - 1 
        # for z in range(len(x)):
        #     start = x[z]
        #     end = x[y]
        #     y -= 1
        #     if start != end:
        #         return False
        # return True
        l,r = 0, len(s) - 1

        while l < r:
            while l < r and not self.isalphanum(s[l]):
                l += 1
            while r > l and not self.isalphanum(s[r]):
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l,r = l + 1, r - 1
        return True

    def isalphanum(self, c):
        return (ord('A') <= ord(c) <= ord('Z') or 
                ord('a') <= ord(c) <= ord('z') or
                ord('0') <= ord(c) <= ord('9'))