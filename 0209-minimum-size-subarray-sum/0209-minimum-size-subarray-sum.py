class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        mini = float('inf') 
        l = 0
        sum = 0
        
        for i in range(n):
            sum += nums[i]
            
            while sum >= target: 
                mini = min(mini, i - l + 1)
                sum -= nums[l]
                l += 1  
        
        return 0 if mini == float('inf') else mini
