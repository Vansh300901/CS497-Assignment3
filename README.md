# CS497-Assignment3

CS-497 Assignment 3

1. Question 1

   A binary search tree is basically a tree where the left node is less than the root value and the right node is greater than the root value.
   So we will make the root of the tree as the middle most element in the array/list and partition the list into 2 parts: left and right
   And to initialize its left node, we will pass the left side of the array/list recursively until there's no element left
   Similarly, to initialize its right node, we will pass the right side of the array/list recursively until there's no element left

   Time complexity: O(n) because we are iterating through an element only once
   Space complexity: O(n) because we are creating a node for each element in the list, hence n nodes in total

2. Question 2

   Preorder traversal has: root, left node, right node
   Inorder traversal has: left node, root, right node

   So we initialize the root with the first value in the preorder list
   Then we find the index where is the root located in the inorder list.
   This gives us an idea of which all elements belong to the left subtree and which all elements belong to the right subtree.
   Then we initialize the root.left subtree with the left half of the inorder traversal
   and initialize the root.right subtree with the right half of the inorder traversal

   Time complexity: O(nlogn) because we iterate through all the elements as well as trying to find its index position in the inorder list
   Space complexity: O(n) because we are creating a node for each element, and in total n nodes.

3. Question 3

   To find the maximum path sum in a binary tree,
   we iterate through all the nodes in the tree and try to compare the left and right subtree.
   The one which has greater value, we add to the root.
   We call the function recursively which calculates the highest sum on the path and returns it.

   Time complexity: O(n) because we are iterating through all the nodes once
   Space complexity: O(1) because we are creating 1 variable to store the highest sum along the path

4. Question 4

   To find the highest element in the row, we start from the root.
   And use a helper function to use the recursive call to itself.

   If we are seeing the very first element on a particular level, then adding it to
   the return list even though it might not be the highest out of all the elements on the same level
   Then once we look at the other nodes at the same level, we keep the one which has the highest value.
   We recursively call the function on the left and right subtree by incrementing the step/level by 1

   Time Complexity: O(n) because we are iterating through all the nodes just once
   Space complexity: O(n). In the worst case scenario, all the elements are on the right subtree of the root
   and in that case, we have each element on its own level and hence we will need n spots in the returnList to
   accomodate n elements.
   But the best case scenario will be O(logn) considering that the tree is balanced.
