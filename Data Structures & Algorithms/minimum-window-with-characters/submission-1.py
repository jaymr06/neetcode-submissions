class Solution:
    def minWindow(self, s: str, t: str) -> str:
        cond = {}
        have = {}
        need = len(t)
        minlength = float('inf')
        minstr = [0, -1]
        l = 0
        for char in t:
            cond[char] = 1 + cond.get(char, 0)

        for r in range(len(s)):
            if have.get(s[r], 0) < cond.get(s[r], 0):
                need -= 1
            have[s[r]] = 1 + have.get(s[r], 0)

            while need == 0:
                if minlength > r - l + 1:
                    minlength = r - l + 1
                    minstr = [l, r]
                if have.get(s[l], 0) <= cond.get(s[l], -1):
                    need += 1
                have[s[l]] -= 1
                l += 1
        return s[minstr[0]:minstr[1] + 1]
