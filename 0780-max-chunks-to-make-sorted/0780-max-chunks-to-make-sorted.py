class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        chunks = 0
        premax=0
        for a in range(len(arr)):
            premax = max(premax,arr[a])
            if premax==a:
                chunks+=1
        return chunks