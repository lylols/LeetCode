class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        ones = 0
        for n in nums:
            if n==1: ones+=1
        one=0
        for i in range(ones):
            if nums[i]==1: one+=1
        mx=one
        l=0
        n= len(nums)
        for r in range(ones,ones+n):
            if nums[l%n]==1:
                one-=1
            l+=1
            if nums[r%n]==1:
                one+=1
            mx= max(mx, one)
        return ones-mx