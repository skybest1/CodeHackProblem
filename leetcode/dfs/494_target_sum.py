class Solution(object):

    def dfs_target_sum_ways(self, nums, i, target):
        """

        :param nums:
        :param i:
        :param target:
        :return:
        """
        if i == len(nums) - 1:
            if nums[i]*(-1) == target or nums[i] == target:
                # print("i: {} num: {} target: {}".format(i, nums[i], target))
                if nums[i] == 0:
                    return 2
                else:
                    return 1
            else:
                return 0
        # if not last num
        dfs1 = self.dfs_target_sum_ways(nums, i+1, target-nums[i])
        # print("i: {} target:{} ways: {}".format(i+1, target-nums[i], dfs1))
        dfs2 = self.dfs_target_sum_ways(nums, i+1, target+nums[i])
        # print("i: {} target:{} ways: {}".format(i + 1, target + nums[i], dfs1))

        return dfs1 + dfs2

    def findTargetSumWays(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return 0
        return self.dfs_target_sum_ways(nums, 0, target)


from unittest import TestCase


class TestSolution(TestCase):

    def test1(self):
        expected = 5
        actual = Solution().findTargetSumWays([1,1,1,1,1], 3)
        self.assertEqual(expected, actual)

    def test2(self):
        expected = 1
        actual = Solution().findTargetSumWays([1], 1)
        self.assertEqual(expected, actual)

    def test3(self):
        expected = 2
        actual = Solution().findTargetSumWays([1, 0], 1)
        self.assertEqual(expected, actual)

    def test4(self):
        expected = 2
        actual = Solution().findTargetSumWays([17,2,1,20,17,36,6,47,5,23,19,9,4,26,46,41,12,11,12,8], 26)
        self.assertEqual(expected, actual)


