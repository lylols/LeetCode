class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n= len(nums)
        c1= c2= None
        cnt1=cnt2=0
        for i in range(n):
            if nums[i]==c1: cnt1+=1
            elif nums[i]== c2: cnt2+=1
            elif cnt1==0: 
                c1= nums[i]
                cnt1=1
            elif cnt2==0: 
                c2= nums[i]
                cnt2=1
            else: 
                cnt1-=1
                cnt2-=1
        
        ans = []
        if nums.count(c1) > len(nums)//3:
            ans.append(c1)
        if nums.count(c2) > len(nums)//3:
            ans.append(c2)
        return ans