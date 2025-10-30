from typing import List

class Solution: 
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        ans = ""  
        for i in range(len(nums)):  # Iterate through the list
            ans += '1' if nums[i][i] == '0' else '0'  # Flip the diagonal element
        return ans


            