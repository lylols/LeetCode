class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        ordered= sorted(heights)
        cnt=0
        for i in range(len(heights)):
            if heights[i] != ordered[i]: cnt+=1
        return cnt
            