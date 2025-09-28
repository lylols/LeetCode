class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r= 0, len(nums)-1
        while l<=r:
            mid = l + (r - l) // 2

            if nums[mid]== target: return mid
            while l<r and nums[l]==nums[mid] and nums[mid]==nums[r]:
                r-=1
                l+=1
                continue
            
            #left sorted
            if nums[mid]>=nums[l]:
                if nums[l]<= target and target<=nums[mid]: r=mid-1
                else: l=mid+1
            #right sorted
            else:
                if nums[mid]<= target and target<=nums[r]: l=mid+1
                else: r= mid-1
        return -1
