class Solution(object):
    def countConsistentStrings(self, allowed, words):
        """
        :type allowed: str
        :type words: List[str]
        :rtype: int
        """
        count=0
        allowed=set(allowed)
        for i in range(len(words)):
            if set(words[i]).issubset(allowed):
                count+=1
        return count

        