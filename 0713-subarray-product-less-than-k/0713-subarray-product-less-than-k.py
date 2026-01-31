class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        l=0
        pro =1
        cnt=0
        #tocnt=0
        for r in range(len(nums)):
            pro*= nums[r]
            while pro>= k and l<=r:
                pro/=nums[l]
                l+=1
            cnt+= r-l+1
            print(cnt)
        return cnt
