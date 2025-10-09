class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        ans=0
        max_diff=0
        max_num=0
        for num in nums:
            ans=max(ans,max_diff*num)
            max_diff=max(max_diff,max_num-num)
            max_num=max(max_num,num)
        return ans