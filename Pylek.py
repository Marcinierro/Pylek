import numpy as np


class TreeType:
    def __init__(self, name, color, texture):
        self.name = name
        self.color = color
        self.texture = texture


class Tree:
    def __init__(self, position, tree_type):
        self.position = position
        self.tree_type = tree_type

    def render(self):
        print(
            f"Rendering {self.tree_type.name} tree at {self.position} with color {self.tree_type.color} and texture {self.tree_type.texture}")


class TreeFactory:
    tree_types = {}

    @staticmethod
    def get_tree_type(name, color, texture):
        key = (name, color, texture)
        if key not in TreeFactory.tree_types:
            TreeFactory.tree_types[key] = TreeType(name, color, texture)
        return TreeFactory.tree_types[key]


if __name__ == "__main__":
    factory = TreeFactory()

    tree1 = Tree(np.array([0, 0]), factory.get_tree_type("Pine", "Green", (0.1, 0.2, 0.3)))
    tree2 = Tree(np.array([10, 10]), factory.get_tree_type("Oak", "Brown", (0.4, 0.5, 0.6)))
    tree3 = Tree(np.array([20, 20]), factory.get_tree_type("Pine", "Green", (0.1, 0.2, 0.3)))

    tree1.render()
    tree2.render()
    tree3.render()
