class Solution:
    def sumOfUnique(self, nums: list[int]) -> int:
        total=0
        for i  in range(len(nums)):
            if nums.count(nums[i])==1:
                total=total+nums[i]
        return total        