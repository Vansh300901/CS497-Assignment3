# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """

        #checking if the length of the array is 0, then returning None
        if len(nums) == 0:
            return None

        #else initializing the middle element to be the root because that means
        #the numbers on its either side are equal
        root = TreeNode(nums[len(nums)//2])

        #calling the function recursively for its left and right subtree with a new list with modified length
        root.left = (self.sortedArrayToBST(nums[:len(nums)//2]))
        root.right = (self.sortedArrayToBST(nums[len(nums)//2+1:]))

        #returning the root
        return root

        