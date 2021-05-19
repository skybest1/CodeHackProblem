from unittest import TestCase


class Solution(object):
    """
        Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of the line i is at (i, ai) and (i, 0). Find two lines, which, together with the x-axis forms a container, such that the container contains the most water.
        Notice that you may not slant the container.

    """

    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        print("input: {}".format(height))
        left_index = []
        right_index = []
        for i in range(0, len(height)):
            if len(left_index) == 0 or height[left_index[-1]] < height[i]:
                left_index.append(i)

        for i in range(len(height)-1, -1, -1):
            if len(right_index) == 0 or height[right_index[-1]] < height[i]:
                right_index.append(i)
        #
        print("left: {}".format(left_index))
        print("right: {}".format(right_index))
        #
        max_result = 0
        left_ptr = 0
        right_ptr = 0
        while left_index[left_ptr] < right_index[right_ptr]:
            container = (right_index[right_ptr]-left_index[left_ptr]) * \
                        (min(height[right_index[right_ptr]], height[left_index[left_ptr]]))
            max_result = max(max_result, container)
            if height[left_index[left_ptr]] < height[right_index[right_ptr]]:
                left_ptr += 1
            else:
                right_ptr += 1
            if (left_ptr > len(left_index) -1) or (right_ptr > len(right_index) - 1):
                break
        return max_result


class TestSolution(TestCase):

    def test1(self):
        height = [1,8,6,2,5,4,8,3,7]
        expected_result = 49
        actual_result = Solution().maxArea(height)
        self.assertEqual(expected_result, actual_result)

    def test2(self):
        height = [1,1]
        expected_result = 1
        actual_result = Solution().maxArea(height)
        self.assertEqual(expected_result, actual_result)

    def test3(self):
        height = [4,3,2,1,4]
        expected_result = 16
        actual_result = Solution().maxArea(height)
        self.assertEqual(expected_result, actual_result)

    def test4(self):
        height = [1,2,1]
        expected_result = 2
        actual_result = Solution().maxArea(height)
        self.assertEqual(expected_result, actual_result)

    def test5(self):
        height = [10,9,8,7,6,5,4,3,2,1]
        expected_result = 25
        actual_result = Solution().maxArea(height)
        self.assertEqual(expected_result, actual_result)


