import unittest


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):

    def do_revert(self, current, next):
        """
            revert current->next chain,
            return next, next.next
        :param current:
        :param next:
        :return:
        """
        if next is None:
            return current, None
        new_next = next.next
        next.next = current
        return next, new_next

    def revert_linked_list(self, head):
        """
           1 -> 2 > 3 -> 4
           => 4->3 ->2 -> 1
           return 4
        :param head:
        :return:
        """
        if head is None:
            return head
        current, next = head, head.next
        head.next = None
        while next:
            current, next = self.do_revert(current, next)
        return current


class TestSolution(unittest.TestCase):

    def make_node_list(self, x):
        head = None
        tail = None
        for i in range(0, x):
            if head is None and tail is None:
                head = ListNode(i)
                tail = head
            else:
                temp = ListNode(i)
                tail.next = temp
                tail = temp
        return head

    def print_list(self, head):
        current_head = head
        while current_head:
            print(current_head.val)
            current_head = current_head.next

    def test_revert_list(self):
        test_list = self.make_node_list(5)
        self.print_list(test_list)
        s = Solution().revert_linked_list(test_list)
        print("Revert Done")
        self.print_list(s)
