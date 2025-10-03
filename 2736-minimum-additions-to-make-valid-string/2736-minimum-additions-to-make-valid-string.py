class Solution:
    def addMinimum(self, word: str) -> int:
        pattern = "abc"
        i = 0
        additions = 0
        
        for ch in word:
            while ch != pattern[i]:
                additions += 1
                i = (i + 1) % 3
            i = (i + 1) % 3
    
        if i != 0:
            additions += 3 - i
        
        return additions
