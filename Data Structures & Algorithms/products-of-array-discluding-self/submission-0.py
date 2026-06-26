class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        for i in nums:
            if i != 0:
                product *= i
        if nums.count(0) == 1:
            output = [0 for _ in range(len(nums))]
            output[nums.index(0)] = product
        elif nums.count(0) > 1:
            output = [0 for _ in range(len(nums))]
        else:
            output = [int(product / i) for i in nums]
        return output