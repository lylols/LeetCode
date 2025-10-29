class Solution:
    def maxDistinctElements(self, nums: List[int], k: int) -> int:
        nums.sort()
        cookie=kiekoo=float("-inf")
        ans=0
        
        def bs(l,r,num):
            while l<r:
                mid= l+ (r-l)//2

                if mid>= num:
                    r=mid

                elif mid<num:
                    l=mid+1
            return l
        
        for num in nums:
            cookie=bs(num-k,num+k,kiekoo+1)
            if cookie!=kiekoo:ans+=1
            kiekoo= max(kiekoo,cookie)
        return ans
        