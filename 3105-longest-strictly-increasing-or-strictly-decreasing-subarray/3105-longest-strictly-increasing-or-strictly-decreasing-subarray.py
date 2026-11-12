class Solution(object):
    def longestMonotonicSubarray(self, nums):
        count_inc = 1
        count_dec = 1
        maximum = 1

        for i in range(1, len(nums)):

            if nums[i] > nums[i-1]:
                count_inc += 1
            else:
                count_inc = 1

            if nums[i] < nums[i-1]:
                count_dec += 1
            else:
                count_dec = 1

            maximum = max(maximum, count_inc, count_dec)

        return maximum