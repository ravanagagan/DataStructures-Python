class TreeNode:
    def __init__(self, data):
        self.data = data  # whatever data which we want to represent[string, int, float]
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

    def print_tree(self, level):
        if level < self.get_level():
            return
        spaces = '   ' * self.get_level() + ("|__" if self.parent else "")  # we need |__ only for child's so
        print(spaces + self.data)
        if self.children:
            for child in self.children:
                child.print_tree(level)


def build_product_tree():
    root = TreeNode("Global")

    india = TreeNode('India')
    usa = TreeNode('USA')

    gujarat = TreeNode('Gujarat')
    karnataka = TreeNode('Karnataka')

    gujarat.add_child(TreeNode('Ahmedabad'))
    gujarat.add_child(TreeNode('Baroda'))
    karnataka.add_child(TreeNode('Bangluru'))
    karnataka.add_child(TreeNode('Mysore'))

    india.add_child(gujarat)
    india.add_child(karnataka)

    new_jersey = TreeNode('New Jersey')
    california = TreeNode('California')

    new_jersey.add_child(TreeNode('Princeton'))
    new_jersey.add_child(TreeNode('Trenton'))
    california.add_child(TreeNode('San Francisco'))
    california.add_child(TreeNode('Mountain View'))
    california.add_child(TreeNode('Palo Alto'))

    usa.add_child(new_jersey)
    usa.add_child(california)

    root.add_child(india)
    root.add_child(usa)

    return root


if __name__ == '__main__':
    root = build_product_tree()  # this will used to create the tree with ecommerce data

    root.print_tree(1)

    # print(root.children.get_level())  # in this we will get the level of the node

    # for child in root.children:
    #     [print(_.parent.data + ": ", _.data) for _ in child.children]



