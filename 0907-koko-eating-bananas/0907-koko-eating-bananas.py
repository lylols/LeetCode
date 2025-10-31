class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l=1
        r= max(piles)
        hrs=0
        while l<=r:
            m= l+ (r-l)//2
            for i in range(len(piles)):
                hrs += ceil(piles[i]/m)
            if hrs<=h:
                r= m-1
            else:
                l= m+1
            hrs=0
        return l