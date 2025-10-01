class Solution:
    def removeStars(self, s: str) -> str:
        res = ""
        stars = 0
        for i in range(len(s) - 1, -1, -1):
            if s[i] == '*':
                stars += 1      
            else:
                if stars > 0: 
                    stars -= 1
                else:
                    res = s[i] + res   
        return res


