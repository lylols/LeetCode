class Solution:
    def minimumOperations(self, num: str) -> int:
        targets = ["00", "25", "50", "75"]
        n = len(num)
        ans = float('inf')

        for t in targets:
            i = n - 1
            cnt = 0
            found_second = False

            while i >= 0:
                if not found_second:
                    if num[i] == t[1]:
                        found_second = True
                    else:
                        cnt += 1
                else:
                    if num[i] == t[0]:
                        ans = min(ans, cnt)
                        break
                    cnt += 1
                i -= 1
 
        if '0' in num:
            ans = min(ans, n - 1)
        
        return ans if ans != float('inf') else n
