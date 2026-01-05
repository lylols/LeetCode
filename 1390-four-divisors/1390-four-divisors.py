class Solution:
    def sumFourDivisors(self, nums):
        allsum = 0

        for x in nums:
            cnt = 0
            divsum = 0

            for i in range(1, int(x**0.5) + 1):
                if x % i == 0:
                    d1 = i
                    d2 = x // i

                    # perfect square → odd divisors → can't be 4
                    if d1 == d2:
                        cnt = 5
                        break

                    cnt += 2
                    divsum += d1 + d2

                    if cnt > 4:
                        break

            if cnt == 4:
                allsum += divsum

        return allsum
