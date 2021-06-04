"""
给你无向 连通 图中一个节点的引用，请你返回该图的 深拷贝（克隆）。

图中的每个节点都包含它的值 val（int） 和其邻居的列表（list[Node]）。

class Node {
    public int val;
    public List<Node> neighbors;
}

测试用例格式：

简单起见，每个节点的值都和它的索引相同。例如，第一个节点值为 1（val = 1），第二个节点值为 2（val = 2），以此类推。该图在测试用例中使用邻接列表表示。

邻接列表 是用于表示有限图的无序列表的集合。每个列表都描述了图中节点的邻居集。

给定节点将始终是图中的第一个节点（值为 1）。你必须将 给定节点的拷贝 作为对克隆图的引用返回。


# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""


class Solution(object):

    def dfs_build_node(self, old_node, value_node_dict, visited_node_val_set):
        """
            1. if new node not created, create new node
            2. loop over current_nodes's neighbour, if not visited, then dfs_build_node(), if visited, then add into cur neighbour
            3. return
        :return:
        """
        if old_node.val not in value_node_dict:
            new_node = Node(old_node.val)
            value_node_dict[new_node.val] = new_node
        new_node = value_node_dict[old_node.val]
        # if already vistied, then directly return
        if new_node.val in visited_node_val_set:
            return new_node
        # build link to its neighbour
        for old_neighbour_node in old_node.neighbors:
            if old_neighbour_node.val not in value_node_dict:
                new_neighbour_node = Node(old_neighbour_node.val)
                value_node_dict[old_neighbour_node.val] = new_neighbour_node
            new_neighbour_node = value_node_dict[old_neighbour_node.val]
            if new_neighbour_node not in new_node.neighbors:
                new_node.neighbors.append(new_neighbour_node)
        # mark current node as visited
        if new_node.val not in visited_node_val_set:
            visited_node_val_set.add(new_node.val)
        # dfs old node's neighbours
        for old_neighbour_node in old_node.neighbors:
            self.dfs_build_node(old_neighbour_node, value_node_dict, visited_node_val_set)

        return new_node

    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        if not node:
            return None
        value_node_dict = {}
        visited_node_val_set = set()
        return self.dfs_build_node(node, value_node_dict, visited_node_val_set)


