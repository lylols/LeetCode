class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        cnt=0
        for k in range(len(nums)-1,-1,-1):
            l=0
            r=k-1
            while(l<r):
                if nums[l]+nums[r] > nums[k]:
                    cnt+= r-l
                    r-=1
                else:
                    l+=1
        return cnt