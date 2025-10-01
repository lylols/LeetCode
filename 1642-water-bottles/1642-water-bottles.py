class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        drunk= numBottles 
        leftt=0
        while numBottles >=numExchange:
            leftt = numBottles% numExchange
            refill = numBottles//numExchange
            drunk += refill
            numBottles = refill+leftt
        return drunk

