class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        m = nums1 + nums2
        m.sort()
        print(m)
        if len(m) % 2 == 0:
            return (m[ len(m) /2 - 1] + m[len(m) /2 ])  / 2.0
        else:
            return m[ len(m) /2 ]
        