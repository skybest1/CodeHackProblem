# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None



class Solution(object):
    def getTargetCopy(self, original, cloned, target):
        """
        :type original: TreeNode
        :type cloned: TreeNode
        :type target: TreeNode
        :rtype: TreeNode
        """
        stack = []
        clone_stack = []

        ptr = original
        clone_ptr = cloned

        result = None
        # compare target to current node
        while ptr or stack:
            if ptr == target:
                print(ptr.val)
                result = clone_ptr
                break
            while(ptr):
                if ptr == target:
                    return clone_ptr
                stack.append(ptr)
                clone_stack.append(clone_ptr)
                ptr = ptr.left
                clone_ptr = clone_ptr.left
            # root outstack
            ptr = stack.pop(-1).right
            clone_ptr = clone_stack.pop(-1).right
        return result


