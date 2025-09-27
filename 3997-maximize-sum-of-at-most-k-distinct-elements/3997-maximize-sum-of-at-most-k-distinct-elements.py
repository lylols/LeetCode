class Solution:
    def maxKDistinct(self, nums: List[int], k: int) -> List[int]:
        nums.sort(reverse=True)
        j=0
        for i in range(len(nums)):
            if(nums[i]!=nums[j]):
                j+=1
                nums[j]=nums[i]
        if j<k: return nums[:j+1]
        res=[]
        for si in range(k):
            res.append(nums[si])
        return res
        return 
        