class Solution:
    def reorganizeString(self, s: str) -> str:
        n = len(s)
        freq = [0] * 26
        
        # Step 1: count frequency and find max frequency
        max_freq = 0
        max_char = 0
        for c in s:
            idx = ord(c) - ord('a')
            freq[idx] += 1
            if freq[idx] > max_freq:
                max_freq = freq[idx]
                max_char = idx
        
        # Step 2: check feasibility
        if max_freq > (n + 1) // 2:
            return ""
        
        # Step 3: initialize result list
        res = [''] * n
        index = 0
        
        # Step 4: place the most frequent character first
        while freq[max_char] > 0:
            res[index] = chr(max_char + ord('a'))
            index += 2
            freq[max_char] -= 1
        
        # Step 5: place remaining characters
        for i in range(26):
            while freq[i] > 0:
                if index >= n:
                    index = 1  # switch to odd indices
                res[index] = chr(i + ord('a'))
                index += 2
                freq[i] -= 1
        
        return "".join(res)
