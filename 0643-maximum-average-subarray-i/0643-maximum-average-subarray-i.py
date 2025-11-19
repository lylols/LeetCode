class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        sumk= sum(nums[:k])
        maxk=sumk
        if k== len(nums): return sumk/k
        for i in range(k, len(nums)):
            sumk = sumk - nums[i-k] + nums[i] 
            maxk = max(maxk, sumk) 
        return maxk/k