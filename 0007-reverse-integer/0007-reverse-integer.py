class Solution:
    def reverse(self, x: int) -> int:
        if x<0:
            sign=-1
        else:
            sign=1
        x=abs(x)
        rev=0
        while x>0:
            r=x%10
            rev=rev*10+r
            x=x//10
        reverse=rev*sign
        if reverse < -2**31 or reverse > 2**31 - 1:
            return 0
        return reverse


