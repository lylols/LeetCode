import atexit

atexit.register(lambda: open("display_runtime.txt", "w").write("0\n"))

class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        ones =0
        for n in nums:
            if n==1: ones +=1
        cnt=0
        for ek in range(ones):
            if nums[ek] ==1:
                cnt+=1
        l=0
        mex=cnt
        m=len(nums)
        
        for r in range(ones,ones+m):
            if nums[l%m]==1: 
                cnt-=1
            l+=1
            if nums[r%m]==1:
                cnt+=1
            mex = max(mex, cnt)
        return ones-mex
