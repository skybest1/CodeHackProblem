import math
from collections import deque


class Solution():

    def full_square_num(self, target_num):
        """
            Pass
        :param target_num:
        :return:
        """
        num_range = int(math.sqrt(target_num))
        queue = deque()
        num_count = 1

        for i in range(1, num_range+1):
            if i**2 == target_num:
                return num_count
            else:
                queue.append(i**2)

        while len(queue) > 0:
            num_count = num_count + 1

            size = len(queue)
            for counter in range(size):
                cur_num = queue.popleft()

                for num in range(1, num_range+1):
                    num_sqr = num**2
                    if cur_num + num_sqr == target_num:
                        return num_count
                    elif cur_num + num_sqr > target_num:
                        break
                    elif cur_num + num_sqr < target_num:
                        queue.append(cur_num+num_sqr)
        return num_count


if __name__ == '__main__':
    print(Solution().full_square_num(2))
