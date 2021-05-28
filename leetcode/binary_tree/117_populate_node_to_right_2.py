"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""


class Solution(object):

    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if not root:
            return root

        queue = []
        queue.append(root)

        while queue:
            counter = len(queue)
            temp_node = queue.pop(0)
            if temp_node.left:
                queue.append(temp_node.left)
            if temp_node.right:
                queue.append(temp_node.right)

            for i in range(counter-1):
                temp_node2 = queue.pop(0)
                temp_node.next = temp_node2
                temp_node = temp_node2
                if temp_node2.left:
                    queue.append(temp_node2.left)
                if temp_node2.right:
                    queue.append(temp_node2.right)
        return root


class Solution2(object):

    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        pass

