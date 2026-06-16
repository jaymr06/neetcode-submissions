class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return self.strToFreq(s) == self.strToFreq(t)
    
    def strToFreq(self, s):
        sDict = {}
        for sSub in s:
            if sSub in sDict:
                sDict[sSub] += 1
            else:
                sDict[sSub] = 1
        return sDict

