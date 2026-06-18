class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for num in nums:
            if num not in freq:
                freq[num] = 1
            else:
                freq[num] += 1
        output = []
        for i in range(k):
            output.append(sorted(freq.items(), key = lambda x: -x[1])[i][0])
        return output
