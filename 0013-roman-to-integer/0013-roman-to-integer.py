class Solution:
    def romanToInt(self, s: str) -> int:
        rmap = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
        }
        ans = rmap[s[len(s)-1]]
        for i in range(len(s)-2,-1,-1):
            if rmap[s[i]] < rmap[s[i+1]]:
                ans-= rmap[s[i]]
            else: ans+= rmap[s[i]]
        return ans 