class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mini= prices[0]
        best=0
        for i in range(1,len(prices)):
            #if prices[i]< mini:
                mini = min(mini, prices[i])
            #else : 
                best= max(best, prices[i]-mini)
        return best