class Solution:
    def doesAliceWin(self, s: str) -> bool:
        vow = "aeiouAEIOU"
        for ch in s:
            if ch in vow: 
                return True
        return False