class Solution:
    def maxDepth(self, s: str) -> int:
        cnt=0
        maxx=0
        for l in s:
            if l == "(": cnt+=1
            elif l== ")": cnt-=1
            maxx = max(cnt, maxx)
        return maxx