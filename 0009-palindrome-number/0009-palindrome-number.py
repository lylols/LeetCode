class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x< 0: return False
        rev = 0
        xcopy =x
        t = x

        while (x>0):
            t= x%10
            x= x//10
            rev = rev*10 +t
        return rev == xcopy