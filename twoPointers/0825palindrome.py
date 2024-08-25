class Solution:
    def isPalindrome(self, s: str) -> bool:
        word = "".join(s.lower() for char in s if s.isalnum())
        return word == word[::-1];

class SolutionTwo:
    def isPalindromeTwo(self, s: str) -> bool:
        l, r = 0, len(s)  - 1;

        while l < r:
            while l < r and not (s[l].isalnum()) :
                l += 1 ;
            while r > l and not (s[r].isalnum()):
                r -= 1 ; 
            if s[l].lower() != s[r].lower() :
                return False;
            l, r = l + 1, r - 1
        return True;

    def alphaNum(self, c):
        return ((ord('A') <= ord('c') <= ord('Z'));
        (ord('a') <= ord('c') <= ord('z')); 
        (ord('0') <= ord('c') <= ord('9'));)





def main():
    testString = "Was it a car or a cat I saw?";
    # print(Solution().isPalindrome(testString));
    print(SolutionTwo().isPalindromeTwo(testString))

if __name__ == "__main__":
    main();