class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n= len(cardPoints)
        total = sum(cardPoints)
        if k==n : return total

        win = n-k
        cham = sum(cardPoints[:win])
        exsum= cham
        for i in range(win,n):
            cham+= cardPoints[i] -cardPoints[i-win]
            exsum = min(cham,exsum)
        return total - exsum