class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left_sum = 0
        nums_sum = sum(nums)
        for i, num in enumerate(nums):
            if left_sum == nums_sum - (left_sum + num):
                return i
            left_sum += num
        else:
            return -1
            
        