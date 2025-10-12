class Solution:
    def makeIntegerBeautiful(self, n: int, target: int) -> int:
        def digit_sum(x):
            s = 0
            while x:
                s += x % 10
                x //= 10
            return s

        p = n
        if digit_sum(n) <= target:
            return 0

        i = 1
        while digit_sum(n) > target:
            rem = n % (10 ** i)
            n = n - rem + (10 ** i)
            i += 1

        return n - p

        
        
