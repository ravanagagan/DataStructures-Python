# Here is how your main function should will look like,
#
# if __name__ == '__main__':
#     root_node = build_management_tree()
#     root_node.print_tree("name") # prints only name hierarchy
#     root_node.print_tree("designation") # prints only designation hierarchy
#     root_node.print_tree("both") # prints both (name and designation) hierarchy

class TreeNode:
    def __init__(self, name, designation):
        self.name = name  # whatever data which we want to represent[string, int, float]
        self.designation = designation
        self.children = []  # this will list it will contain the TreeNode instance
        self.parent = None  # it will store the parent of TreeNode class means child

    def add_child(self, child):
        child.parent = self  # we are adding child to self so always child.parent should be self
        self.children.append(child)

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent  # by going backwards based on parent will get the level
        return level

    def print_tree(self, property_name):
        if property_name == 'both':
            value = self.name + " ( " + self.designation + ")"
        elif property_name == 'name':
            value = self.name
        else:
            value = self.designation

        spaces = '   ' * self.get_level() + ("|__" if self.parent else "")  # we need |__ only for child's so
        print(spaces + value)
        if self.children:
            for child in self.children:
                child.print_tree(property_name)


def build_product_tree():
    root = TreeNode("Nilupul", "CEO")

    CTO = TreeNode('Chinmay', "CTO")
    HR_Head = TreeNode('Gels', 'HR Head')

    Infra_Head = TreeNode('Vishwa', 'Development Manager')
    CTO.add_child(Infra_Head)
    CTO.add_child(TreeNode('Amir', 'Application Head'))

    HR_Head.add_child(TreeNode('Peter', 'Recruitment Manager'))
    HR_Head.add_child(TreeNode('Waqus', 'Policy Manager'))

    Infra_Head.add_child(TreeNode('Dhaval', 'Cloud Manager'))
    Infra_Head.add_child(TreeNode('Gagan', 'App Manager'))

    root.add_child(CTO)
    root.add_child(HR_Head)

    return root


if __name__ == '__main__':
    root = build_product_tree()  # this will used to create the tree with ecommerce data

    root.print_tree("designation")

    # print(root.children.get_level())  # in this we will get the level of the node

    # for child in root.children:
    #     [print(_.parent.data + ": ", _.data) for _ in child.children]
