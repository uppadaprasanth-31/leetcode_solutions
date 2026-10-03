class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for i in range(len(haystack)):
            j=0
            while j<len(needle) and i+j<len(haystack):
                if haystack[i+j]!= needle[j]:
                    break
                j=j+1
            if j==len(needle):
                return i
        return -1
        