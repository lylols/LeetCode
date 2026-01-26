class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        summ=0
        n= len(cost)
        m= n%3
        cost.sort()
        for i in range(n):
            if i%3==m:
                continue
            summ+=cost[i]
        return summ
