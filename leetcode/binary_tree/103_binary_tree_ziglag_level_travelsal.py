# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

import math

class Solution(object):

    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        final_result = []

        left_stack = []
        right_stack = []

        if root:
            left_stack.append(root)

        while left_stack or right_stack:
            if left_stack:
                temp_result = []
                while left_stack:
                    element = left_stack.pop(-1)
                    temp_result.append(element.val)
                    if element.left:
                        right_stack.append(element.left)
                    if element.right:
                        right_stack.append(element.right)
                final_result.append(temp_result)
                continue
            elif right_stack:
                temp_result = []
                while right_stack:
                    element = right_stack.pop(-1)
                    temp_result.append(element.val)
                    if element.right:
                        left_stack.append(element.right)
                    if element.left:
                        left_stack.append(element.left)
                final_result.append(temp_result)
        return final_result
