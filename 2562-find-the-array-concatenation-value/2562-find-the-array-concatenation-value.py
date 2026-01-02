class Solution:
    def findTheArrayConcVal(self, nums: List[int]) -> int:
        l=0
        r= len(nums)-1
        smu=0
        while l<=r:
            if l==r:
                smu+= nums[l]
                return smu
            smu+= int(str(nums[l])+str(nums[r]))
            l+=1
            r-=1
        return smu