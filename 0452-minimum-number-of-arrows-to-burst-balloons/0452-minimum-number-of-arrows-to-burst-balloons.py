class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key= lambda x: x[1])
        prev= points[0][1]
        cnt=1
        for s,e in points:
            if s> prev:
                cnt+=1
                prev = e
        return cnt