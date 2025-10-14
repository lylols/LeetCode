class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        p = k 

        for i in range(n - k): 
            temp_k = k
            j = i

            while temp_k > 1 and j + 1 < n - k and nums[j] < nums[j + 1] and nums[j + k] < nums[j + k + 1]:
                temp_k -= 1
                j += 1

            if temp_k == 1:  
                return True

        return False

