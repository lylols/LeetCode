class Solution:
    def partitionDisjoint(self, nums: list[int]) -> int:
        n = len(nums)
        rightMin = [0] * n
        rightMin[-1] = nums[-1]
       
        for i in range(n - 2, -1, -1):
            rightMin[i] = min(nums[i], rightMin[i + 1])
        
        leftMax = nums[0]
        for i in range(n - 1):
            leftMax = max(leftMax, nums[i])
            if leftMax <= rightMin[i + 1]:
                return i + 1
        
        return n - 1
