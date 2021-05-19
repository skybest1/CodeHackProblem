

def partition(array, left, right):
    # track smallest index
    small_idx = left - 1
    piovt = array[right]
    # loop over left, to right-1, if element < piovt, swap with small_idx
    for big_idx in range(left, right):
        if array[big_idx] <= piovt:
            small_idx += 1
            array[small_idx], array[big_idx] = array[big_idx], array[big_idx]
    # swap small_idx+1 with right
    array[small_idx+1], array[right] = array[right], array[small_idx+1]
    return small_idx + 1


def quick_sort(array, left, right):
    if len(array) == 1:
        return
    if left >= right:
        return
    partition_index = partition(array, left, right)
    quick_sort(array, left, partition_index-1)
    quick_sort(array, partition_index+1, right)


if __name__ == '__main__':
    array = [1]
    quick_sort(array, 0, len(array)-1)
    print(array)

    test = [[3, 2], [2, 10], [1, 22]]
    test.sort(key=lambda item: item[0])
    print(test)
