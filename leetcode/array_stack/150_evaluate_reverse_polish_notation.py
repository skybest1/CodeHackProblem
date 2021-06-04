"""
Evaluate the value of an arithmetic expression in Reverse Polish Notation.

Valid operators are +, -, *, and /. Each operand may be an integer or another expression.

Note that division between two integers should truncate toward zero.

It is guaranteed that the given RPN expression is always valid. That means the expression would always evaluate to a result,
and there will not be any division by zero operation.

Input: tokens = ["2","1","+","3","*"]
Output: 9
Explanation: ((2 + 1) * 3) = 9

"""


class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        from collections import deque

        operator = ['+', '-', '*', '/']
        stack = deque()

        for i in range(len(tokens)):
            cur_token = tokens[i]
            if cur_token not in operator:
                stack.append(cur_token)
                continue
            # calculate expression
            num2 = int(stack.pop())
            num1 = int(stack.pop())
            if cur_token == '+':
                calculated_value = num1 + num2
            elif cur_token == '-':
                calculated_value = num1 - num2
            elif cur_token == '*':
                calculated_value = num1 * num2
            elif cur_token == '/':
                calculated_value = int(num1/num2)
            stack.append(calculated_value)
            print("{} {} {} = {}".format(num1, cur_token, num2, calculated_value))
        return int(stack.pop())



from unittest import TestCase


class TestSolution(TestCase):

    def test1(self):
        input = ["2","1","+","3","*"]
        expected = 9
        actual = Solution().evalRPN(input)
        self.assertEqual(expected, actual)

    def test2(self):
        input = ["4","13","5","/","+"]
        expected = 6
        actual = Solution().evalRPN(input)
        self.assertEqual(expected, actual)

    def test3(self):
        input = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
        expected = 22
        actual = Solution().evalRPN(input)
        self.assertEqual(expected, actual)

    def test4(self):
        input = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
        expected = 22
        actual = Solution().evalRPN(input)
        print("actual :{} expected: {}".format(actual, expected))
        self.assertEqual(expected, actual)



