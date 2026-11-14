class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i=0
        res=1
        while i<2 and nums:
            res=res*(max(nums)-1)
            nums.remove(max(nums))
            i+=1
        return res 
