"""
Given a list, rotate the list to the right by k places, where k is non-negative.

For example:
Given 1->2->3->4->5->NULL and k = 2,
return 4->5->1->2->3->NULL.
"""

# Definition for singly-linked list.


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        real_length = self.get_length(head)
        if real_length == 0:
            return head
        real_shift = k % real_length
        if real_shift == 0:
            return head
        # get new tail
        new_tail = head
        for i in range(0, real_length-real_shift-1):
            new_tail = new_tail.next

        # get new head
        new_head = new_tail.next

        # set new tail
        new_tail.next = None

        # set old tail
        old_tail = new_head
        while True:
            if old_tail.next is None:
                break
            else:
                old_tail = old_tail.next
        old_tail.next = head
        return new_head

    def get_length(self, head):
        temp = head
        length = 0
        while True:
            if temp is None:
                break
            else:
                length = length + 1
                temp = temp.next
        return length

    def display(self, head):
        temp = head
        while temp is not None:
            print temp.val
            temp = temp.next


if __name__ == '__main__':
    l1 = ListNode(1)
    l2 = ListNode(2)
    l3 = ListNode(3)
    l4 = ListNode(4)
    l1.next = l2
    l2.next = l3
    l3.next = l4

    s1 = Solution()

    s1.display(head=s1.rotateRight(l1, 3))
