class Solution:
    def minRemoval(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        l = 0
        max_window = 0

        for r in range(n):
            while nums[l] * k < nums[r]:
                l += 1
            max_window = max(max_window, r - l + 1)

        return n - max_window
