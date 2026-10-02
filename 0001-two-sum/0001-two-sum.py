class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        j=len(nums)
        result=[]
        for i in range(len(nums)):
            for j in range(0,len(nums)):
                if nums[i]+nums[j]==target and i!=j:
                    result=[i,j]
        return result