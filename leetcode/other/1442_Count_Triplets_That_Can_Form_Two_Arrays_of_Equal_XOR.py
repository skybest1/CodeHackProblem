"""
Given an array of integers arr.

We want to select three indices i, j and k where (0 <= i < j <= k < arr.length).

Let's define a and b as follows:

a = arr[i] ^ arr[i + 1] ^ ... ^ arr[j - 1]
b = arr[j] ^ arr[j + 1] ^ ... ^ arr[k]
Note that ^ denotes the bitwise-xor operation.

Return the number of triplets (i, j and k) Where a == b.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/count-triplets-that-can-form-two-arrays-of-equal-xor

presum[j] = arr[0]^arr[1]^...^arr[j]

1, 1, 1

0, 1, 2, 3

p[0, 1] = p[2] - p[0] = p[j+1] - p[i]
p[i, j] = p[j+1] - p[i]

presum(i, j) = arr[i]^arr[i+1]^...^arr[j] = presum[i-1]^presum[j]

用array的index

p[i, j] = p[i]^p[j+1]


a = arr[i] ^ arr[i + 1] ^ ... ^ arr[j - 1] = b = arr[j] ^ arr[j + 1] ^ ... ^ arr[k]

=> p[i, j-1] = p[j, k]

p[i]^p[j] = p[j]^p[k+1]

p[i] = p[k+1]

0<=i<k<=len(array)

i=1, k=3

"""

from unittest import TestCase

class Solution(object):
    def countTriplets(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        [0, 1]

        [0, 0, 1]
        p[0, 1] = p[0]^p[2] = 0^1 = 1
        """
        psums = []
        current_sum = 0
        psums.append(current_sum)
        for i in range(0, len(arr)):
            current_sum = current_sum ^ arr[i]
            psums.append(current_sum)
        #
        # print(arr)
        # print(psums)
        current_result = 0
        for i in range(0, len(arr)):
            for k in range(len(arr)-1, 0, -1):
                if k <= i:
                    break
                if psums[i] == psums[k+1]:
                    current_result += (k-i)
        return current_result


class TestSolution(TestCase):

    def test0(self):
        arr = [2,3,1,6,7]
        expected = 4
        actual = Solution().countTriplets(arr)
        self.assertEqual(expected, actual)

    def test1(self):
        arr = [1,1,1,1,1]
        expected = 10
        actual = Solution().countTriplets(arr)
        self.assertEqual(expected, actual)

    def test3(self):
        arr = [2,3]
        expected = 0
        actual = Solution().countTriplets(arr)
        self.assertEqual(expected, actual)

    def test4(self):
        arr = [1,3,5,7,9]
        expected = 3
        actual = Solution().countTriplets(arr)
        self.assertEqual(expected, actual)

    def test5(self):
        arr = [7,11,12,9,5,2,7,17,22]
        expected = 8
        actual = Solution().countTriplets(arr)
        self.assertEqual(expected, actual)
