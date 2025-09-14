class Solution:
    def maxArrayValue(self, nums: List[int]) -> int:
        maxx =0
        if len(nums)==1: return nums[0]
        for i in range(len(nums)-1,0,-1):
            if nums[i] >= nums[i-1] : nums[i-1]= nums[i] + nums[i - 1]
            maxx = max(maxx, nums[i-1])
        return maxx