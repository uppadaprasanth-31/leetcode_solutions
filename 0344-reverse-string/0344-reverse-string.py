class Solution:
    def reverseString(self, s: list[str]) -> None:
        i=0 
        j=len(s)-1
        while i<=j and j>=0:
            s[i], s[j] = s[j], s[i]
            i=i+1
            j=j-1

        return "".join(s)
        
    
        