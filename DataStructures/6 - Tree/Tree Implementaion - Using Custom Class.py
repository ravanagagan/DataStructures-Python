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

    def print_tree(self):
        spaces = '   ' * self.get_level() + ("|__" if self.parent else "")  # we need |__ only for child's so
        print(spaces + self.data)
        if self.children:
            for child in self.children:
                child.print_tree()


def build_product_tree():
    root = TreeNode("Electronics")

    laptop = TreeNode('Laptop')
    laptop.add_child(TreeNode('Acer'))
    laptop.add_child(TreeNode('Lenovo'))
    laptop.add_child(TreeNode('Dell'))

    cellphone = TreeNode('Cell phone')
    cellphone.add_child(TreeNode('MI'))
    cellphone.add_child(TreeNode('Samsung'))
    cellphone.add_child(TreeNode('Nokia'))

    tv = TreeNode('TV')
    tv.add_child(TreeNode('Samsung'))
    tv.add_child(TreeNode('NVY'))
    tv.add_child(TreeNode('Sharp'))

    root.add_child(laptop)
    root.add_child(cellphone)
    root.add_child(tv)

    return root


if __name__ == '__main__':
    root = build_product_tree()  # this will used to create the tree with ecommerce data

    root.print_tree()

    # print(root.children.get_level())  # in this we will get the level of the node

    # for child in root.children:
    #     [print(_.parent.data + ": ", _.data) for _ in child.children]



