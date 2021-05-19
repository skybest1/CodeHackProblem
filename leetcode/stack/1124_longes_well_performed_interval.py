
class Solution1(object):

    def longestWPI(self, hours):
        """
        :type hours: List[int]
        :rtype: int
        """
        standard_list = []
        for hour in hours:
            standard_value = -1
            if hour > 8:
                standard_value = 1
            standard_list.append(standard_value)
        # calculate the sum
        prefix_sum_arry = self.calculation_prefix_sum_array(standard_list)
        return self.calculate_wpi(standard_list, prefix_sum_arry, 0, len(standard_list)-1)

    def calculation_prefix_sum_array(self, array):
        """

        :param array:
        :return: list of n+1 len, array[i] stores sum of first i elements. from 0 to i-1
        """
        prefix_sum_array = []
        current_sum = 0
        prefix_sum_array.append(current_sum)
        for i in range(0, len(array)):
            current_sum += array[i]
            prefix_sum_array.append(current_sum)
        return prefix_sum_array

    def get_sum(self, array, prefix_sum_array, left, right):
        """

        :param array:
        :param prefix_sum_array:
        :param left:
        :param right:
        :return:
        """
        if left == right:
            return array[left]
        result = prefix_sum_array[right+1] - prefix_sum_array[left]
        return result

    def calculate_wpi(self, standard_list, sum_array, left, right):
        if left == right:
            if standard_list[left] > 0:
                return 1
            else:
                return 0
        #
        sum = self.get_sum(standard_list, sum_array, left, right)
        if sum > 0:
            return right-left+1
        else:
            max1 = self.calculate_wpi(standard_list, sum_array, left+1, right)
            max2 = self.calculate_wpi(standard_list, sum_array, left, right-1)
            return max(max1, max2)


class Solution2(object):

    def longestWPI(self, hours):
        """
        :type hours: List[int]
        :rtype: int
        """
        standard_hour = []
        for hour in hours:
            std_hour = -1
            if hour > 8:
                std_hour = 1
            standard_hour.append(std_hour)
        # calculate presums
        presums = []
        presums.append(0)
        current_sum = 0
        for std_hour in standard_hour:
            current_sum += std_hour
            presums.append(current_sum)

        size = len(hours)
        # 1, 1, 1
        # 0, 1, 2, 3
        # sum(1, 2) = 2 = pre(3) - pre(1) = 2
        # sum(i, j) = presum(j) - presum(i-1)
        max_size = 0
        for i in range(0, len(presums)):
            for j in range(i+1, len(presums)):
                if presums[j] - presums[i] > 0:
                    max_size = max(max_size, (j-i))
        return max_size


class Solution3(object):

    def longestWPI(self, hours):
        """
        :type hours: List[int]
        :rtype: int
        """
        standard_hour = []
        for hour in hours:
            std_hour = -1
            if hour > 8:
                std_hour = 1
            standard_hour.append(std_hour)
        # calculate presums
        presums = []
        presums.append(0)
        current_sum = 0
        for std_hour in standard_hour:
            current_sum += std_hour
            presums.append(current_sum)

        size = len(hours)
        # 1, 1, 1
        # 0, 1, 2, 3
        # sum(1, 2) = 2 = pre(3) - pre(1) = 2
        # sum(i, j) = presum(j) - presum(i-1)
        stack = []
        for i in range(0, len(presums)):
            if len(stack) == 0:
                stack.append(i)
            elif presums[stack[-1]] > presums[i]:
                stack.append(i)
        # stack
        print(presums)
        print(stack)
        max_size = 0
        for i in range(len(presums)-1, -1, -1):
            if len(stack) == 0:
                break
            if presums[i] < presums[stack[-1]]:
                continue
            while len(stack) > 0:
                stack_idx = stack[-1]
                if presums[i] > presums[stack_idx]:
                    stack.pop(-1)
                    max_size = max(max_size, i-stack_idx)
                else:
                    break
        return max_size


if __name__ == '__main__':
    s = Solution3()
    array = [9,6,6]
    wpi = s.longestWPI(array)
    print(wpi)




