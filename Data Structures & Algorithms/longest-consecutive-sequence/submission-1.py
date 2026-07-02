class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        for num in nums:
            if num - 1 in nums:
                continue
            currLen = 1
            for i in range(1, len(nums)):
                if num + i in nums:
                    currLen += 1
                else:
                    break
            if currLen > longest:
                longest = currLen
        return longest

            
            

        