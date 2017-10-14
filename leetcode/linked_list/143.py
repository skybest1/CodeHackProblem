"""
Given a singly linked list L: L0L1...Ln-1Ln,
reorder it to: L0LnL1Ln-1L2Ln-2
You must do this in-place without altering the nodes values
For example,Given {1,2,3,4}, reorder it to {1,4,2,3}
"""



import unittest


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        length = self.get_list_length(head)
        half_len = int(length/2)
        head1 = head
        tail1 = None
        head2 = head
        # find head 2
        for i in range(half_len):
            head2 = head2.next
            if i == half_len-2:
                tail1 = head2
        # set tail1
        tail1.next = None
        # reverse list2
        new_head2 = self.reverse_list(head2)
        # merge list1 and list2

    def merge_lists(self, head1, head2):
        current = None
        index1 = head1
        index2 = head2
        new_head = head1
        counter = 0
        next = index2
        while True:
            

    def get_list_length(self, head):
        temp = head
        length = 0
        while True:
            if temp is None:
                break
            else:
                length += 1
                temp = temp.next


    def reverse_list(self, head):
        if head is None:
            return head

        temp = head.next
        head.next = None
        return self.do_reverse_list(head, temp)

    def do_reverse_list(self, current, next):
        if next is None:
            return current
        temp = next.next
        next.next = current
        return self.do_reverse_list(next, temp)


class TestSolution(unittest.TestCase):

    def make_node_list(self, x):
        head = None
        tail = None
        for i in range(1, x):
            if head is None and tail is None:
                head = ListNode(i)
                tail = head
            else:
                temp = ListNode(i)
                tail.next = temp
                tail = temp
        return head


    def make_test_print(self, head):
        head = head
        while True:
            if head is None:
                break
            else:
                print head.val
                head = head.next
        assert True

    def test_reverse(self):
        head = self.make_node_list(5)
        new_head = Solution().reverse_list(head)
        while True:
            if new_head is not None:
                print new_head.val
                new_head = new_head.next
            else:
                break