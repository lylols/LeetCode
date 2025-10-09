class Solution:
    def minimumSum(self, nums: List[int]) -> int:
        n = len(nums)
        left_min = [float('inf')] * n
        right_min = [float('inf')] * n

        # Compute left smaller
        min_left = nums[0]
        for i in range(1, n):
            if min_left < nums[i]:    
                left_min[i] = min_left
            min_left = min(min_left, nums[i])

        # Compute right smaller
        min_right = nums[-1]
        for i in range(n-2, -1, -1):
            if min_right < nums[i]:     
                right_min[i] = min_right
            min_right = min(min_right, nums[i])

        # Find minimum sum
        min_sum = float('inf')
        for i in range(1, n-1):
            if left_min[i] != float('inf') and right_min[i] != float('inf'):
                min_sum = min(min_sum, nums[i] + left_min[i] + right_min[i])

        return min_sum if min_sum != float('inf') else -1
