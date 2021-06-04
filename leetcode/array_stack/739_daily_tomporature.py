"""
    Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead.
Example 1:

Input: temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]
Example 2:

Input: temperatures = [30,40,50,60]
Output: [1,1,1,0]
Example 3:

Input: temperatures = [30,60,90]
Output: [1,1,0]
"""


class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        from collections import deque

        result_list = [0]*len(temperatures)
        stack = deque()

        for i in range(len(temperatures)):
            if len(stack) == 0:
                stack.append(i)
                continue

            cur_temp = temperatures[i]
            # pop out all temp in stack where temp less than cur_temp, and populate result_list
            while stack:
                stack_temp_index = stack.pop()
                if temperatures[stack_temp_index] < cur_temp:
                    result_list[stack_temp_index] = i - stack_temp_index
                    continue
                else:
                    stack.append(stack_temp_index)
                    break
            stack.append(i)
        return result_list


from unittest import TestCase

class TestSolution(TestCase):

    def test1(self):
        input = [73,74,75,71,69,72,76,73]
        expected = [1,1,4,2,1,1,0,0]
        actual = Solution().dailyTemperatures(input)
        self.assertEqual(expected, actual)

    def test2(self):
        input = [30,40,50,60]
        expected = [1,1,1,0]
        actual = Solution().dailyTemperatures(input)
        self.assertEqual(expected, actual)

    def test3(self):
        input = [30,60,90]
        expected = [1,1,0]
        actual = Solution().dailyTemperatures(input)
        self.assertEqual(expected, actual)

    def test4(self):
        input = [1, 1, 1]
        expected = [0, 0, 0]
        actual = Solution().dailyTemperatures(input)
        self.assertEqual(expected, actual)
