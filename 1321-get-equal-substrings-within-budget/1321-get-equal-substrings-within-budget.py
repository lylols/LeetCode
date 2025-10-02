class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        left = 0
        currCost = 0
        maxLen = 0

        for right in range(len(s)):
            currCost += abs(ord(s[right]) - ord(t[right]))

            while currCost > maxCost:
                currCost -= abs(ord(s[left]) - ord(t[left]))
                left += 1

            maxLen = max(maxLen, right - left + 1)

        return maxLen


