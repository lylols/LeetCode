class Solution:
    def largestInteger(self, num: int) -> int:
        even =[]
        odd = []
        digits = [int(d) for d in str(num)]

        for d in digits:
            if d % 2 == 0:
                even.append(d)
            else: odd.append(d)

        even.sort(reverse=True)
        odd.sort(reverse=True)

        # Reconstruct result with parity preserved
        res = []
        ei, oi = 0, 0
        for d in digits:
            if d % 2 == 0:
                res.append(even[ei])
                ei += 1
            else:
                res.append(odd[oi])
                oi += 1

        return int(''.join(map(str, res)))
