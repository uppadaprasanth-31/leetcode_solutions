class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        res=""
        k=0
        for i in s:
            for j in range(k,len(t)):
                if i==t[j]:
                    res=res+i
                    k=j+1
                    break

        if s==res:
            return True
        else:
            return False
            
