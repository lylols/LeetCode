class Solution:
    def minimumSum(self, nums: List[int]) -> int:
        minsu= 200
        for i in range(1,len(nums)-1):
            l=i-1
            r= i+1
            minl, minr= 51,51
            for l in range(i):
                if nums[l] < nums[i]:
                    minl = min(minl, nums[l])

            for r in range(i + 1, len(nums)):
                if nums[r] < nums[i]:
                    minr= min(minr, nums[r])

            if minl != 51 and minr != 51:
                minsu = min(minsu, nums[i] + minl + minr)
        return minsu if minsu != 200 else -1
                