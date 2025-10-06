class Solution:
    def myAtoi(self, s: str) -> int:
        ans=""
        i=0
        while i< len(s) and s[i]==" ": i+=1
        if i < len(s) and s[i] in "+-":
            ans += s[i]
            i += 1
        while i< len(s):
            if s[i] == " ":
                break
            elif not s[i].isdigit(): break
            else: 
                ans+= s[i]
            i+=1
        if ans in ("", "+", "-"):
            return 0
            
        num = int(ans)
        INT_MIN, INT_MAX = -2**31, 2**31 - 1
        return max(INT_MIN, min(INT_MAX, num))


