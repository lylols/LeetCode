class Solution:
    def minimumLevels(self, possible: List[int]) -> int:
        prefix = [1 if possible[0] == 1 else -1]
        for i in range(1, len(possible)):
            if possible[i] == 0:
                prefix.append(prefix[-1] - 1)
            else:
                prefix.append(prefix[-1] + 1)
        
        for i in range(len(prefix)-1):
            if prefix[i] > prefix[-1] - prefix[i]:
                return i+1
        
        return -1