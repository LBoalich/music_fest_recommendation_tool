from Tree_Node import TreeNode
from data import *

#create Tree
root_node = TreeNode("Music Festivals")

camping_node = TreeNode('Camping')
camping_node.set_parent(root_node)
root_node.add_child(camping_node)

non_camping_node = TreeNode('Non-Camping')
non_camping_node.set_parent(root_node)
root_node.add_child(non_camping_node)
