from Tree_Node import TreeNode

def add_Tree_Node(new_value, parent_node):
    new_node = TreeNode(new_value)
    new_node.set_parent(parent_node)
    parent_node.add_child(new_node)

