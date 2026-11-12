class Solution(object):
    def leftRightDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ls=0
        rs=0
        i=0
        lst=[]
        for i in range(len(nums)):
            ls=sum(nums[:i])
            rs=sum(nums[i+1:])
            lst.append(abs(ls-rs))
        return lst






        