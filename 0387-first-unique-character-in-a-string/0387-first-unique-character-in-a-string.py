class Solution:
    def firstUniqChar(self, s: str) -> int:
        for i in range(len(s)):
            j = 0

            while j < len(s):
                if i != j and s[i] == s[j]:
                    break
                j += 1

            if j == len(s):
                return i

        return -1