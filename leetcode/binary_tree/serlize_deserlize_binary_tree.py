# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

            1
        2       3

        1,2,#,#,3,#,#

        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return '#'
        return str(root.val)+','+self.serialize(root.left)+','+self.serialize(root.right)

    def make_node(self, node_str_list):
        """

        :param node_str_list:
        :return:
        """
        cur_node_val = node_str_list.pop(0)
        if cur_node_val == '#':
            return None
        cur_node = TreeNode(int(cur_node_val))
        if node_str_list:
            cur_node.left = self.make_node(node_str_list)
        if node_str_list:
            cur_node.right = self.make_node(node_str_list)
        return cur_node

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        "1,2,#,#,3,#,#"

        :type data: str
        :rtype: TreeNode
        """
        node_str_list = data.split(',')
        result = self.make_node(node_str_list)
        return result



# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))