class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if "-" in str(n) or n == 0:
            return False
        return (math.log(n) / math.log(4)).is_integer()
        