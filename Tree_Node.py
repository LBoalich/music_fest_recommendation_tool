class TreeNode:
    def __init__(self, value, parent = None):
        self.value = value 
        self.parent = parent
        self.children = []
 
    def add_child(self, child_node):
        self.children.append(child_node) 
    
    def remove_child(self, child_node):
        print("Removing " + child_node.value + " from " + self.value)
        self.children = [child for child in self.children 
                        if child is not child_node]

    def set_parent(self, parent):
        if isinstance(parent, TreeNode):
            self.parent = parent
        else:
            return "Error: Must be instance of Tree Node"

    def get_parent(self):
        return self.parent
 
    def traverse(self):
        nodes_to_visit = [self]
        while len(nodes_to_visit) > 0:
            current_node = nodes_to_visit.pop()
            print(current_node.value)
            nodes_to_visit += current_node.children
