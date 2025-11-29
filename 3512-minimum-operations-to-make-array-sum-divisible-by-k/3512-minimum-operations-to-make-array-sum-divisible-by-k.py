class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        summ= sum(nums)
        if summ< k: return summ
        else: return summ%k