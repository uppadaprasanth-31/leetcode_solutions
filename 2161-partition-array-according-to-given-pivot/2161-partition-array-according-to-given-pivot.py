class Solution(object):
    def pivotArray(self, nums, pivot):
        """
        :type nums: List[int]
        :type pivot: int
        :rtype: List[int]
        """
        lst1=[]
        lst2=[]
        lst3=[]
        for i in range(len(nums)):
            if nums[i]<pivot:
                lst1.append(nums[i])
            elif nums[i]==pivot:
                lst2.append(nums[i])
            else:
                lst3.append(nums[i])
        return lst1+lst2+lst3
        