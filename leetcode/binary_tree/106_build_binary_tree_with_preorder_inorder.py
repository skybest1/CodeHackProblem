# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):

    def do_build_tree(self, inorder, postorder, left, right, inorder_dict):
        """
            build a root node, for subtree, from [left, right] in postorder
                    inorder:   left_tree, root, right_tree
                    postorder: left_tree, right_tree, root
        :param inorder:
        :param postorder:
        :param left:
        :param right:
        :param inorder_dict:
        :return:
        """
        if left == right:
            return TreeNode(postorder[right], None, None)
        # last node in postorder is it's root
        cur_node_val = postorder[right]
        cur_node = TreeNode(postorder[right], None, None)
        cur_node_inorder_index = inorder_dict[cur_node_val]
        # deal with left tree
        left_start = left
        left_end = left - 1
        while (left_end + 1 <= right-1) and inorder_dict[postorder[left_end+1]] < cur_node_inorder_index:
            left_end += 1
        # no left tree
        if left_start <= left_end:
            cur_node.left = do_build_tree(inorder, postorder, left_start, left_end, inorder_dict)
        # deal with right tree
        right_start = left_end + 1
        right_end = right - 1
        if right_start <= right_end:
            cur_node.right = do_build_tree(inorder, postorder, right_start, right_end, inorder_dict)
        # return current root
        return cur_node

    def buildTree(self, inorder, postorder):
        """
        inorder:   left_tree, root, right_tree
        postorder: left_tree, right_tree, root
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        if not inorder:
            return None

        inorder_dict = dict()
        for i in range(len(inorder)):
            value = inorder[i]
            inorder_dict[value] = i
        return self.do_build_tree(inorder, postorder, 0, len(postorder)-1, inorder_dict)

