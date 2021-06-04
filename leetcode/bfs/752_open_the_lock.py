"""
You have a lock in front of you with 4 circular wheels.
Each wheel has 10 slots: '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'. The wheels can rotate freely and wrap around: for example we can turn '9' to be '0', or '0' to be '9'. Each move consists of turning one wheel one slot.
The lock initially starts at '0000', a string representing the state of the 4 wheels.
You are given a list of deadends dead ends, meaning if the lock displays any of these codes, the wheels of the lock will stop turning and you will be unable to open it.
Given a target representing the value of the wheels that will unlock the lock, return the minimum total number of turns required to open the lock, or -1 if it is impossible.
 
Example 1:

Input: deadends = ["0201","0101","0102","1212","2002"], target = "0202"
Output: 6
Explanation:
A sequence of valid moves would be "0000" -> "1000" -> "1100" -> "1200" -> "1201" -> "1202" -> "0202".
Note that a sequence like "0000" -> "0001" -> "0002" -> "0102" -> "0202" would be invalid,
because the wheels of the lock become stuck after the display becomes the dead end "0102".

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/open-the-lock
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
import collections
import queue
class Solution(object):

    def do_change_number(self, num_str, index):
        """

        :param num_str:
        :param index:
        :return: list of new number
        """
        cur_digit = int(num_str[index])
        next_digit_list = [str((cur_digit+1)%10), str((cur_digit-1)%10)]
        result_list = []
        for next_digit_str in next_digit_list:
            candidate_str = num_str[:index] + next_digit_str + num_str[index+1:]
            result_list.append(candidate_str)
        return result_list

    def change_number(self, num_str):
        result_list = []
        for i in range(0, len(num_str)):
            result_list.extend(self.do_change_number(num_str, i))
        return result_list

    def openLock(self, deadends, target):
        """
        '0000' -> target
            should not in deadends
        :type deadends: List[str]
        :type target: str
        :rtype: int
        """
        start = '0000'
        if start in deadends:
            return -1
        deadend_set = set(deadends)
        queue = collections.deque()
        step = 0
        find = False
        queue.append(start)

        checked_num = set()

        while len(queue) > 0:
            size = len(queue)
            for i in range(size):
                cur_num = queue.popleft()
                # return if is target
                if cur_num == target:
                    return step
                # if not then move to next step
                checked_num.add(cur_num)
                next_candidate = self.change_number(cur_num)
                next_candidate = [num for num in next_candidate if (num not in deadend_set) and (num not in checked_num)]
                queue.extend(next_candidate)
            step = step + 1
        return -1


if __name__ == '__main__':
    print(Solution().openLock(["8887","8889","8878","8898","8788","8988","7888","9888"], "8888"))
