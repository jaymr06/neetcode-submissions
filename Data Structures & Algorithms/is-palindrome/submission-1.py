class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join(char for char in s if char.isalpha() or char.isnumeric()).lower()
        length = len(s)
        i = 0
        while i < length // 2:
            if not s[i] == s[-(i+1)]:
                return False
            i += 1
        return True
        