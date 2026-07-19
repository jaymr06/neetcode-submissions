class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        output = []
        nums = sorted(nums)
        for i in range(len(nums)):
            if nums[i] > 0:
                break
            l, r = i+1, len(nums) - 1
            while l < r:
                if nums[i] + nums[l] + nums[r] < 0:
                    l += 1
                elif nums[i] + nums[l] + nums[r] > 0:
                    r -= 1
                else:
                    if [nums[i], nums[l], nums[r]] not in output:
                        output.append([nums[i], nums[l], nums[r]])
                    l += 1
        return output
        
                

        
        