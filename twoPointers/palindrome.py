class Solution:
    def isPalindrome(self, s: str) -> bool:
        while l < r:
            if s[l].lower() != s[r].lower():
                return False



    def alphaNum(self, c):
        (ord('A') <= ord(c) <= ord('Z'));
        (ord('a') <= ord(c) <= ord('z'));
        (ord('0') <= ord(c) <= ord('9'));



    
    class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(c.lower() for c in s if c.isalnum())
        return s == s[::-1]
