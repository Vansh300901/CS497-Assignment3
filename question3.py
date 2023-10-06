# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):

    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        # returnList to keep track of the maximum sum of the path
        returnList = []

        #adding the root to the returnList because at the moment the root is the highest value
        returnList.append(root.val)

        def recursiveDFS(root):
            #checking if the root is None, then returning 0
            if root is None:
                return 0

            #finding the value of the left subtree
            left = recursiveDFS(root.left)
            #checking which one is greater, left subtree or 0
            left = max(0, left)

            #similarly finding the value of the right subtree and checking which one is greater, right subtree or 0
            right = recursiveDFS(root.right)
            right = max(0, right)

            #checking which one is greater, the value we have in the returnlist or the summation of nodes in the path
            returnList[0] = max(left + right + root.val, returnList[0])

            #returning the sum of the root and the maximum of the left and right tree
            return (root.val + max(left, right))

        recursiveDFS(root)
        return returnList[0]
