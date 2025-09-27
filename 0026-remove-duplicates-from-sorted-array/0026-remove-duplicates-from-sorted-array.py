class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i,j=0,0
        for i in range(len(nums)):
            if(nums[i]!= nums[j]):
                j+=1
                nums[j]=nums[i]
        return j+1