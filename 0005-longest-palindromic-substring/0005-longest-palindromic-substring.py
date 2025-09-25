class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand(l: int, r: int) -> str:
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            return s[l+1:r]

        res = ""
        for i in range(len(s)):
            # odd length
            res = max(res, expand(i, i), key=len)
            # even length
            res = max(res, expand(i, i+1), key=len)
        return res
