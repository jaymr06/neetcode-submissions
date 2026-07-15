class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1
        while True:
            sum = numbers[l] + numbers[r]
            if sum < target:
                l = l + 1
            elif sum > target:
                r = r - 1
            else:
                return [l + 1, r + 1]