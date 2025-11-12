class Solution:
    def minimalKSum(self, nums: List[int], k: int) -> int:
        nums = sorted(set(nums))  # remove duplicates and sort
        summ = 0
        curr = 1

        for num in nums:
            if num > curr:
                count = min(k, num - curr)
                summ += (count * (2*curr + count - 1)) // 2
                k -= count
                if k == 0:
                    return summ
            curr = num + 1 

        if k > 0:
            summ += (k * (2*curr + k - 1)) // 2
        
        return summ
