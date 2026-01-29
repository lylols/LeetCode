class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        if len(nums)<2: return 0
        nums.sort()
        minnu= inf
        l=0
        for r in range(k-1,len(nums)):
            minnu = min(minnu, nums[r]-nums[l])
            l+=1
        return minnu