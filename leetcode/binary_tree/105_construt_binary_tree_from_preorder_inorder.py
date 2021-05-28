# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):

    def build_node(self, preorder, inorder, inorder_dict, left, right):
        """
            preorder: root, left_tree, right_tree
            inorder:  left_tree, root, right_tree
        """
        # leaf node, directly create Node
        if left == right:
            return TreeNode(preorder[left], None, None)
        current_root_value = preorder[left]
        current_node = TreeNode(current_root_value, None, None)
        # find its left child range in preorder
        current_root_inorder_idx = inorder_dict[current_root_value]
        # deal with left
        left_start_idx = left + 1
        left_end_idx = left
        while left_end_idx + 1 <= right and inorder_dict[preorder[left_end_idx + 1]] < current_root_inorder_idx:
            left_end_idx += 1
        if left_start_idx > left_end_idx:
            current_node.left = None
        else:
            current_node.left = self.build_node(preorder, inorder, inorder_dict, left_start_idx, left_end_idx)
        # deal with right
        right_end_idx = right
        right_start_idx = right + 1

        while right_start_idx - 1 > left and inorder_dict[preorder[right_start_idx - 1]] > current_root_inorder_idx:
            right_start_idx -= 1
        if right_start_idx > right_end_idx:
            current_node.right = None
        else:
            current_node.right = self.build_node(preorder, inorder_dict, inorder_dict, right_start_idx, right_end_idx)

        return current_node

    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if not preorder:
            return None

        inorder_dict = dict()
        for i in range(len(inorder)):
            inorder_dict[inorder[i]] = i
        return self.build_node(preorder, inorder, inorder_dict, 0, len(preorder) - 1)

