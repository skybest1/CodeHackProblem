"""
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.
Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

Example 1:

Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.
Example 2:

Input: nums = [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
Total amount you can rob = 2 + 9 + 1 = 12.

1 <= nums.length <= 100
0 <= nums[i] <= 400


take[i] stores the max sum of money can rob if take nums[i]
skip[i] store the max sum of money can rob if skip nums[i]


take[i] = skip[i] + nums[i]
skip[i] = max(take[i-1], skip[i-1])

return max (max(take), max(skip))

"""


from unittest import TestCase


class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]
        elif len(nums) == 2:
            return max(nums)
        #
        take = [0]*len(nums)
        skip = [0]*len(nums)

        take[0] = nums[0]
        skip[0] = 0

        for i in range(1, len(nums)):
            take[i] = skip[i-1] + nums[i]
            skip[i] = max(take[i-1], skip[i-1])

        # print("nums: {}".format(nums))
        # print("take: {}".format(take))
        # print("skip: {}".format(skip))
        return max(max(take), max(skip))


class TestSolution(TestCase):

    def test1(self):
        input1 = [1,2,3,1]
        expected = 4
        actual = Solution().rob(input1)
        self.assertEqual(expected, actual)

    def test2(self):
        input1 = [2,7,9,3,1]
        expected = 12
        actual = Solution().rob(input1)
        self.assertEqual(expected, actual)

    def test3(self):
        input1 = [9, 1, 1, 8]
        expected = 17
        actual = Solution().rob(input1)
        self.assertEqual(expected, actual)



