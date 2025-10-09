class Solution:
    def minimumSum(self, nums: List[int]) -> int:
        n = len(nums)
        suf_min = [0] * n
        suf_min[-1] = nums[-1]

        for i in range(n-2, -1, -1):
            suf_min[i] = min(nums[i], suf_min[i+1])
        
        preMin = nums[0]
        ans = inf
        for j in range(1, n-1):
            if preMin < nums[j] > suf_min[j+1]:
                ans = min(ans, preMin + nums[j] + suf_min[j+1])
            
            preMin = min(preMin, nums[j])
        
        return ans if ans != inf else -1