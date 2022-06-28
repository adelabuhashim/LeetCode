class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if sum(nums[1:]) == 0:
            return 0
        for i in range(1, len(nums)-1):
            if sum(nums[:i]) == sum(nums[i+1:]):
                return i

        if sum(nums[:-1]) == 0:
            return len(nums) - 1 
        return -1
            
        