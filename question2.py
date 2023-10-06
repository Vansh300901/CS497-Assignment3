# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """

        # checking if there's no element left in the preorder and inorder list, then returning None
        if not len(preorder) or not len(inorder):
            return None

        # making the first element in the preorder list as the root
        root = TreeNode(preorder[0])

        # finding the location of that root element in the inorder tree
        middleElem = inorder.index(preorder[0])

        #recursively calling the same function to set the left node of the tree with inorder list as only the left half of it
        #because it belongs to the left side
        root.left = self.buildTree(preorder[1:middleElem+1], inorder[:middleElem])

        #recursively calling the same function to set the right node of the tree  with inorder list as only the right half of it
        #because it belongs to the right side
        root.right = self.buildTree(preorder[middleElem+1:], inorder[middleElem+1:])

        #returning the root
        return root
        