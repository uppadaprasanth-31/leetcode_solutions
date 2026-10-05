class Solution:
    def scoreOfString(self, s: str) -> int:
        a=[ord(ch) for ch in s]
        res=0
        j=1
        for i in a:
            if j<len(a):
                res=res+abs(i-a[j])
                j=j+1
        return res
            
           
        
