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

    def do_connect(self, node1, node2):
        """
            node1.next = node2
            do_connect (node1.left, node1.right)
            do_connect(node1.right, node2.left)
            do_connect(node2.left, node2.right)
        :param node:
        :return:
        """
        if node1 and node2:
            node1.next = node2

        if node1 and node2 and node1.left and node1.right and node2.left and node2.right:
            self.do_connect(node1.left, node1.right)
            self.do_connect(node1.right, node2.left)
            self.do_connect(node2.left, node2.right)
        return

    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if not root:
            return root
        self.do_connect(root.left, root.right)
        current = root
        while current:
            current.next = None
            current = current.right
        return root


class Solution2(object):

    def connect(self, root):
        """
            take each layer as linked list
            connect from l1 to l2
            when connect l2, travel on l1
        :type root: Node
        :rtype: Node
        """
        if not root:
            return root

        cur = root

        while cur:

            temp_node = Node(0, None, None, None)
            ptr = temp_node

            while cur:

                if cur.left:
                    ptr.next = cur.left
                    ptr = ptr.next
                if cur.right:
                    ptr.next = cur.right
                    ptr = ptr.next
                cur = cur.next
            # cur point to next level's start
            cur = temp_node.next
        return root

