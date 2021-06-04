class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])
        # print("m: {} n:{}".format(m, n))
        land_set = set()
        # add all '1'
        for i in range(0, m):
            for j in range(0, n):
                if grid[i][j] == '1':
                    land_set.add((i, j))
        #
        total_num = 0

        while land_set:
            # print("land_set: {}".format(land_set))
            temp_set = set()
            sample_pos = list(land_set)[0]
            queue = []
            queue.append(sample_pos)
            # print("sample pos: {}".format(sample_pos))
            while queue:
                (cur_i, cur_j) = queue.pop(0)
                # add it's neigbour '1' into queue if exist in land_set ()
                # left
                if cur_i >0 and grid[cur_i-1][cur_j] == '1':
                    if (cur_i-1, cur_j) not in temp_set:
                        queue.append((cur_i - 1, cur_j))
                        # print("add1: {}".format((cur_i-1, cur_j)))
                # right
                if cur_i < m -1 and grid[cur_i+1][cur_j] == '1':
                    # temp_set.add((cur_i+1, cur_j))
                    if (cur_i+1, cur_j) not in temp_set:
                        queue.append((cur_i+1, cur_j))
                        # print("add2: {}".format((cur_i + 1, cur_j)))
                # down
                if cur_j >0 and grid[cur_i][cur_j-1] == '1':
                    # temp_set.add((cur_i, cur_j-1))
                    if (cur_i, cur_j-1) not in temp_set:
                        # print("add3: {}".format((cur_i, cur_j - 1)))
                        queue.append((cur_i, cur_j-1))
                # up
                if cur_j < n-1 and grid[cur_i][cur_j+1] == '1':
                    # print("add4: {}".format((cur_i, cur_j+1)))
                    # temp_set.add((cur_i, cur_j+1))
                    if (cur_i, cur_j+1) not in temp_set:
                        # print("add4: {}".format((cur_i, cur_j + 1)))
                        queue.append((cur_i, cur_j+1))
                # fully travelled
                temp_set.add((cur_i, cur_j))
                # print("Add {} to traveled list.".format((cur_i, cur_j)))
            # one loop over
            total_num += 1
            # print("temp_set:{}".format(temp_set))
            land_set = land_set - temp_set
        return total_num




if __name__ == '__main__':
    input = [["1","1","1","1","0"],
             ["1","1","0","1","0"],
             ["1","1","0","0","0"],
             ["0","0","0","0","0"]
             ]
    print(Solution().numIslands(input))