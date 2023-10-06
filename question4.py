# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):

    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """

        #initializing a return list
        returnList = []

        #using a helper function with root, returnList and step = 0
        self.helperFunction(root, returnList, 0)

        #returning the returnList
        return returnList

    def helperFunction(self, root, returnList, step):

        #checking if the root is none, then returning
        if root is None:
            return

        # checking if we are at seeing the very first element on that particular step (level), then adding it to the
        # return list even if it is not the highest one.
        if len(returnList) == step:
            returnList.append(root.val)
        else:
            # if it is not the first element, then keeping the value whichever one is the highest
            returnList[step] = max(returnList[step], root.val)

        # recursively calling the same function on the left Subtree and right Subtree with increasing the step by 1
        self.helperFunction(root.left, returnList, step + 1)
        self.helperFunction(root.right, returnList, step + 1)
