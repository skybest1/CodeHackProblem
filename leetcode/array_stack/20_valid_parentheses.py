"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
"""


class Solution(object):
    def isValid(self, s):
        """

        :type s: str
        :rtype: bool
        """
        if s == "":
            return True

        from collections import deque
        stack = deque()
        for i in range(len(s)):
            cur_char = s[i]
            if cur_char in ['(', '{', "["]:
                stack.append(cur_char)
                continue
            elif cur_char in [')', '}', ']'] and len(stack) == 0:
                return False
            else:
                pop_char = stack.pop()
                if cur_char == ')' and pop_char != '(':
                    return False
                if cur_char == '}' and pop_char != '{':
                    return False
                if cur_char == ']' and pop_char != '[':
                    return False
        if len(stack) == 0:
            return True
        else:
            return False


