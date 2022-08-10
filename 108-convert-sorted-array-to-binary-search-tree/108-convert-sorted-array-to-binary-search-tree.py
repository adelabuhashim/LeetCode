# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        print( nums)
        if not nums:
            return None
        m = len(nums) // 2 
        return TreeNode(nums[m],self.sortedArrayToBST(nums[:m]),              # <-- left  subtree
                             self.sortedArrayToBST(nums[m+1:]))            # <-- right subtree
        
        
