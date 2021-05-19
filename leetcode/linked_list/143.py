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
        if length <= 2:
            return head
        half_len = int(length/2)
        head1 = head
        tail1 = head
        head2 = head
        # find head 2
        for i in range(half_len):
            head2 = head2.next
            if i == half_len-2:
                tail1 = head2
        # set tail1
        tail1.next = None
        # reverse list2
        new_head2 = self.new_reverse_list(head2)
        # merge list1 and list2
        merged_head = self.merge_lists(head1, new_head2)
        head = merged_head

    def merge_lists(self, head1, head2):
        index1 = head1
        index2 = head2
        new_head = head1
        counter = 0
        current = index1
        index1 = index1.next
        while True:
            if index1 == None or index2 == None:
                break
            counter += 1
            if counter % 2 == 1:
                current.next = index2
                current = index2
                index2 = index2.next
            else:
                current.next = index1
                current = index1
                index1 = index1.next
        if index1 == None:
            current.next = index2
        else:
            current.next = index1
        return new_head
            

    def get_list_length(self, head):
        temp = head
        length = 0
        while True:
            if temp is None:
                break
            else:
                length += 1
                temp = temp.next
        return length


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

    def new_reverse_list(self, head):
        if head is None:
            return head

        current = head
        next = head.next
        head.next = None
        while True:
            if next is None:
                return current
            temp = next.next
            next.next = current
            current = next
            next = temp
        return current


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
                print(head.val)
                head = head.next
        assert True

    def test_reverse(self):
        head = self.make_node_list(5)
        new_head = Solution().new_reverse_list(head)
        self.make_test_print(new_head)
        assert True

    def test_merge(self):
        list1 = self.make_node_list(2)
        head = Solution().reorderList(list1)
        #self.make_test_print(head)
        #assert True