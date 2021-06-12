# """
# arra_a and arr_b is array contains none-negative numbers.
# one operation is +1 or -1 on one element in arr_a or arr_b
# how many operations do we need at least
# to let max element in A, not greater than min element in B?
#
# A start from 0 i
#
# B start from tail  j
#
#
# for a[i] > b_min
# b[j] < a_max
#
# return min( a[i]-b_min + func(arr_a, arr_b, i+1, j), a_max - b[j] + func(arr_a, arr_b, i, j-1))
#
# """

from unittest import TestCase


class Solution(object):


    def do_calculate_min_step(self, arr_a, arr_b, index_a, index_b):
        """

        :param arr_a: sorted arr_a
        :param arr_b: sorted arr_b
        :param index_a:
        :param index_b:
        :return:
        """
        a_max = arr_a[len(arr_a)-1]
        b_min = arr_b[0]

        if index_a > len(arr_a) - 1 or index_b < 0:
            return 0
        # index_a
        while index_a <= len(arr_a) - 1:
            if arr_a[index_a] <= b_min:
                index_a += 1
            else:
                break
        # index_b
        while index_b >= 0:
            if arr_b[index_b] >= a_max:
                index_b -= 1
            else:
                break
        # deal with index_a and index_b
        if index_a > len(arr_a) - 1 or index_b < 0:
            return 0
        result_a = arr_a[index_a] - b_min + self.do_calculate_min_step(arr_a, arr_b, index_a+1, index_b)
        result_b = a_max - arr_b[index_b] + self.do_calculate_min_step(arr_a, arr_b, index_a, index_b-1)
        return min(result_a, result_b)

    def calculate_min_step(self, arr_a, arr_b):
        """

        :param arr_a:
        :param arr_b:
        :return: int num
        """
        return self.do_calculate_min_step(arr_a, arr_b, 0, len(arr_b)-1)


class TestSolution(TestCase):

    def test1(self):

        arr_a = [1, 2, 7]
        arr_b = [3, 4, 8]
        expected = 4
        actual = Solution().calculate_min_step(arr_a, arr_b)
        self.assertEqual(expected, actual)

    def test2(self):

        arr_a = [1, 2, 3]
        arr_b = [4, 4, 8]
        expected = 0
        actual = Solution().calculate_min_step(arr_a, arr_b)
        self.assertEqual(expected, actual)


    def test3(self):
        arr_a = [1, 6, 6, 7]
        arr_b = [5, 10, 12]
        expected = 2
        actual = Solution().calculate_min_step(arr_a, arr_b)
        self.assertEqual(expected, actual)

