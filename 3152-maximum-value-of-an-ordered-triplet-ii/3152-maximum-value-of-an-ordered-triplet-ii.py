class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        n= len(nums)
        rmax= [0]*n
        rmax[-1]= nums[-1]

        for i in range(n-2,-1,-1):
            rmax[i]= max(nums[i], rmax[i+1])

        lmax= nums[0]
        maxval= -inf
        for i in range(1,n-1):
            #if lmax > nums[i] and rmax[i]> nums[i]:
            maxval = max(maxval, (lmax- nums[i])*rmax[i+1])
            lmax = max(lmax, nums[i])

        return maxval if maxval >0 else 0