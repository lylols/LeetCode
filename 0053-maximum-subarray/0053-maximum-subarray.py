class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sum=0
        maxx= -10**4
        for i in range(len(nums)):
            sum+= nums[i]
            maxx= max(maxx, sum)
            if sum<0: sum=0
        return maxx
