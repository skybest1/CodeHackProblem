from unittest import TestCase


class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        stack = []

        for element in path.split('/'):
            if element not in ['', '.', '..']:
                stack.append(element)
            if element == '..' and stack:
                stack.pop(-1)
        result = "/"+"/".join(stack)
        return result


class TestSolution(TestCase):

    def test1(self):
        input = "/home/"
        expected = "/home"
        actual = Solution().simplifyPath(input)
        self.assertEqual(expected, actual)

    def test2(self):
        input = "/../"
        expected = "/"
        actual = Solution().simplifyPath(input)
        self.assertEqual(expected, actual)

    def test3(self):
        input = "/home//foo/"
        expected = "/home/foo"
        actual = Solution().simplifyPath(input)
        self.assertEqual(expected, actual)

    def test4(self):
        input = "/a/./b/../../c/"
        expected = "/c"
        actual = Solution().simplifyPath(input)
        self.assertEqual(expected, actual)




