class Solution:
    def countWays(self, ranges: List[List[int]]) -> int:
        MOD= 10**9+7
        ranges.sort()
        cnt =1
        end= ranges[0][1]
        for i in range(1,len(ranges)):
            if ranges[i][0] > end:
                end= ranges[i][1]
                cnt+=1
            else :
                end = max(end, ranges[i][1])
        return pow(2, cnt, MOD)