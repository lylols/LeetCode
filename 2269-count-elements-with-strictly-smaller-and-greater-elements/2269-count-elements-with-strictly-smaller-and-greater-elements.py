class Solution:
    def countElements(self, nums: List[int]) -> int:
        if not nums:
            return 0

        n = len(nums)
        minu = maxu = nums[0]
        min_count = max_count = 1

        for i in range(1, n):
            x = nums[i]
            if x < minu:
                minu = x
                min_count = 1
            elif x == minu:
                min_count += 1

            if x > maxu:
                maxu = x
                max_count = 1
            elif x == maxu:
                max_count += 1

        if minu == maxu:
            return 0
        return n - min_count - max_count
