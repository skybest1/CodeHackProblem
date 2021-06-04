"""
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.
"""


class Solution(object):

    def dfs_grid(self, grid, i, j):
        """
            if curnode is 1, then mark current node and it's neighbour node as 0
        :param grid:
        :param i:
        :param j:
        :return:
        """
        n = len(grid[0])
        m = len(grid)

        if i < 0 or i > m-1:
            return
        if j < 0 or j > n-1:
            return
        if grid[i][j] == '0':
            return
        grid[i][j] = '0'
        self.dfs_grid(grid, i-1, j)
        self.dfs_grid(grid, i+1, j)
        self.dfs_grid(grid, i, j-1)
        self.dfs_grid(grid, i, j+1)

    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid:
            return 0
        n = len(grid[0])
        m = len(grid)
        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    self.dfs_grid(grid, i, j)
                    count += 1
        return count


from unittest import TestCase


class TestSolution(TestCase):

    def test2(self):
        input = \
            [
              ["1","1","1","1","0"],
              ["1","1","0","1","0"],
              ["1","1","0","0","0"],
              ["0","0","0","0","0"]
            ]
        expected = 1
        actual = Solution().numIslands(input)
        self.assertEqual(expected, actual)

    def test3(self):
        input = [
              ["1","1","0","0","0"],
              ["1","1","0","0","0"],
              ["0","0","1","0","0"],
              ["0","0","0","1","1"]
        ]
        expected = 3
        actual = Solution().numIslands(input)
        self.assertEqual(expected, actual)
