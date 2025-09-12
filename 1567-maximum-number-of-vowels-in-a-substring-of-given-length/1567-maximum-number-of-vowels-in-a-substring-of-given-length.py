class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vow = 'aeiouAEIOU'
        cnt =0
        for r in range(k):
            if s[r] in vow:
                cnt +=1
        if len(s) >1: l=0
        else : return cnt
        maxx =cnt
        for r in range(k, len(s)): 
            if s[l] in vow: cnt-=1
            if s[r] in vow: cnt+=1
            if l< len(s)-k+1: l+=1
            maxx= max(maxx,cnt)
        return maxx


            