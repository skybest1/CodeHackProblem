from unittest import TestCase


class Solution(object):

    def findMaximumXOR(self, nums):
        """
            Given an integer array nums, return the maximum result of nums[i] XOR nums[j], where 0 ≤ i ≤ j < n.
            Follow up: Could you do this in O(n) runtime?
                1 <= nums.length <= 2 * 10^4
                0 <= nums[i] <= 2^31 - 1

        # 要使得X最大，那么对于二进制的X， 从高到低，每一位尽量取到1
        # 一共31个bit，从第一个到最后一个，确定每一个bit是否可以取到 1
        从最高位开始，去顶是否可以取到最低
        # 异或的性质： z = x^y，则 x = z^y, y=z^x

        # 衍生题： 使得X最小？ 从最高位开始比，每一位尽量取0
        :type nums: List[int]
        :rtype: int
        """
        result = 0

        for n in range(30, -1, -1):
            temp_set = set()
            # add in each set
            for num in nums:
                temp_set.add(num >> n)
            # assume first (31-n) bit of result can be 1
            result = result*2 + 1
            find = False
            for num in nums:
                if ((num>>n) ^ result) in temp_set:
                    find = True
                    break
            if not find:
                result = result - 1
        return result


class SolutionTest(TestCase):
    """
        Input: nums = [2,4]
        Output: 6

        Input: nums = [3,10,5,25,2,8]
        Output: 28
        Explanation: The maximum result is 5 XOR 25 = 28.

        来源：力扣（LeetCode）
        链接：https://leetcode-cn.com/problems/maximum-xor-of-two-numbers-in-an-array
        著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

        Input: nums = [0]
        Output: 0

        Input: nums = [2,4]
        Output: 6

        Input: nums = [8,10,2]
        Output: 10

        Input: nums = [14,70,53,83,49,91,36,80,92,51,66,70]
        Output: 127
    """
    def test1(self):
        nums = [3, 10, 5, 25, 2, 8]
        expected = 28
        acutal = Solution().findMaximumXOR(nums)
        self.assertEqual(acutal, expected)

    def test2(self):
        nums = [2, 4]
        expected = 6
        actual = Solution().findMaximumXOR(nums)
        self.assertEqual(expected, actual)

    def test3(self):
        nums = [8, 10, 2]
        expected = 10
        actual = Solution().findMaximumXOR(nums)
        self.assertEqual(expected, actual)

    def test4(self):
        nums = [14,70,53,83,49,91,36,80,92,51,66,70]
        expected = 127
        actual = Solution().findMaximumXOR(nums)
        self.assertEqual(expected, actual)