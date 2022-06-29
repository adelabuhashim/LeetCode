class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """

        if "-" in str(x):
            x = int(str(x)[1:][::-1]) * -1
            return x if x >= -2 ** 31 else 0 
        else:
            x = int(str(x)[::-1])
            return x if x < 2 **31 else 0
        