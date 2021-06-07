

class QuickSort(object):

    def quick_sort(self, nums):
        """
            Pass
        :param nums:
        :return:
        """
        self.do_quick_sort(nums, 0, len(nums)-1)

    def do_quick_sort(self, nums, left, right):
        partiton = self.partition(nums, left, right)
        if partiton > left:
            self.do_quick_sort(nums, left, partiton-1)
        if partiton < right:
            self.do_quick_sort(nums, partiton+1, right)

    def partition(self, nums, left, right):
        """

        :param nums:
        :param left:
        :param right:
        :return: return partition index
        """
        if left == right:
            return left
        pivot = nums[right]
        left_board = left - 1

        left_ptr = left
        while left_ptr <= right - 1:
            if nums[left_ptr] <= pivot:
                nums[left_board+1], nums[left_ptr] = nums[left_ptr], nums[left_board+1]
                left_board += 1
            left_ptr += 1
        nums[left_board+1], nums[right] = nums[right], nums[left_board+1]
        return left_board + 1


def binary_search(nums, value):
    """

    :param nums:
    :param value:
    :return:
    """
    value = do_binary_search(nums, 0, len(nums)-1, value)
    return value


def do_binary_search(nums, left, right, value):
    if left > right:
        return None
    mid = int((left+right)/2)
    if nums[mid] == value:
        return mid
    elif nums[mid] > value:
        return do_binary_search(nums, left, mid-1, value)
    elif nums[mid] < value:
        return do_binary_search(nums, mid+1, right, value)


def do_binary_search_none_recursive(nums, value):
    """
        binary search
        if there is same number inside the list, return the smallest index
    :param nums: number list
    :param value: search value
    :return: index of search value, return -1 if not found
    """
    result_index = -1

    left = 0
    right = len(nums) - 1
    while left <= right:
        mid = int((left + right)/2)
        if nums[mid] == value:
            if result_index == -1:
                result_index = mid
            else:
                result_index = min(result_index, mid)
            right = mid - 1
        elif nums[mid] < value:
            left = mid + 1
        else:
            right = mid - 1
    return result_index




def longest_increase_sub_array(nums):
    """
        return the length of longest increase sub array
        d[i] = length of longest increase sub array, end with nums[i]
        d[j] = max(d[i]+1, d[j]) if nums[j] > nums[i] and i<j
    :param nums:
    :return:
    """
    d = []
    for i in range(0, len(nums)):
        d.append(1)
    # calculate each d[i]
    for i in range(0, len(nums)):
        for j in range(0, i):
            if nums[i] > nums[j]:
                d[i] = max(d[j]+1, d[i])
    print(d)
    return max(d)


def longest_increase_sub_array_count(nums):
    """
        return the length of longest increase sub array
        d[i] = length of longest increase sub array, end with nums[i]
        d[j] = max(d[i]+1, d[j]) if nums[j] > nums[i] and i<j

        count[i], count of longest increase sub array, end with nums[i]
        if num[i]< num[j] and i<j:
            if d[i] >= d[j]:
                d[j] = d[i] + 1
                count[j] = count[i]
            elif d[i]+1 == d[j]:
                count[j] += count[i]
    :param nums:
    :return:
    """
    if not nums:
        return 0

    length = []
    count = []
    for i in range(0, len(nums)):
        length.append(1)
        count.append(1)
    # calculate each d[i]
    for i in range(0, len(nums)):
        for j in range(0, i):
            if nums[i] > nums[j]:
                if length[i] <= length[j]:
                    length[i] = length[j] + 1
                    count[i] = count[j]
                # multiple longest path found
                elif length[i] == length[j] + 1:
                    count[i] += count[j]

    max_length = max(length)
    max_length_num_idx = [i for i in range(len(nums)) if length[i] == max_length]
    print("max length: {}".format(max_length))
    print("length: {}".format(length))
    print("count: {}".format(count))

    count_sum = 0
    for i in max_length_num_idx:
        count_sum += count[i]

    return count_sum


def find_midium_of_two_sorted_array(array1, array2):
    len1 = len(array1)
    len2 = len(array2)

    ptr1 = -1
    ptr2 = -1

    is_odd = (len1+len2) % 2 == 1
    step_to_go = int((len1 + len2)/2)

    for i in range(step_to_go):
        if ptr1 == len(array1) -1:
            ptr2 += 1
        elif ptr2 == len(array2) - 1:
            ptr1 += 1
        else:
            if array1[ptr1+1] < array2[ptr2+1]:
                ptr1 += 1
            else:
                ptr2 += 1
    #
    if is_odd:
        if ptr1 < len(array1) -1 and ptr2 < len(array2) -1:
            if array1[ptr1+1] < array2[ptr2+1]:
                return (array1[ptr1+1]*2)/2
            else:
                return (array2[ptr2+1]*2)/2
        elif ptr1 == len(array1) -1:
            return (array2[ptr2+1]*2)/2
        elif ptr2 == len(array2) -1:
            return (array1[ptr1+1]*2)/2
    else:

        if ptr1 < len(array1) -1 and ptr2 < len(array2) -1:
            if ptr1 == -1:
                return (array2[ptr2] + min(array1[ptr1+1], array2[ptr2+1]))/2
            elif ptr2 == -1:
                return (array1[ptr1] + min(array1[ptr1+1], array2[ptr2+1]))/2
            else:
                return (max(array1[ptr1], array2[ptr2]) + min(array1[ptr1+1], array2[ptr2+1]))/2
        elif ptr1 == len(array1) -1:
            return (array2[ptr2]+array2[ptr2+1])/2
        elif ptr2 == len(array2) - 1:
            return (array1[ptr1]+array1[ptr1+1])/2


def biggest_sub_arrary_sum(array):
    """
        Pass
    :param array:
    :return:
    """
    pre_sum_array = [0]
    cur_sum = 0
    for i in range(len(array)):
        cur_sum += array[i]
        pre_sum_array.append(cur_sum)
    #
    # sum(i, j) = pre_sum_array[j+1] - presum_array[i]
    result_max = None
    for i in range(len(array)):
        for j in range(i, len(array)):
            current_sum = pre_sum_array[j+1] - pre_sum_array[i]
            if result_max is None:
                result_max = current_sum
            else:
                result_max = max(result_max, current_sum)
    return result_max



if __name__ == '__main__':
    array = [0, 1, -2, 1, -1, -5, -6]
    print(biggest_sub_arrary_sum(array))

