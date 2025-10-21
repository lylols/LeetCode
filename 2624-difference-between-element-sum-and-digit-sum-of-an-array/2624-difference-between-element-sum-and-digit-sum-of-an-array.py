class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        summ = sum(nums)
        elsum=0
        for el in nums:
            while el:
                elsum +=el%10
                el= el//10
        return summ- elsum
        