class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        hm= nums[0]
        nums.sort()
        if nums[0]==hm or nums[1]==hm or nums[2]==hm:
            return sum(nums[:3])
        return hm+ sum(nums[:2])