class BinaryTree(object):
    def __init__(self, value=None, left=None, right=None):
        self.left = left
        self.right = right
        self.value = value

    def maximum(self):
        root = self
        current = self

        while root.right:
            current = root
            root = root.right

        return current, root

    def getSecondMax(self):

        current, root = self.maximum()

        return current.value if root.left == None \
            else root.left.maximum()[1].value

    def _getPartString(self, part, tab):
        noneStr = ' ' * tab + 'None'
        return noneStr if part == None else part._getTreeString(tab)

    def _getTreeString(self, tab):
        nTab = tab + 2
        ftStr = ' ' * tab + '%s\n%s\n%s'
        return ftStr % (self.value,
                        self._getPartString(self.left, nTab),
                        self._getPartString(self.right, nTab))

    def __str__(self):
        return self._getTreeString(0)

    def __repr__(self):
        return '\n' + self._getTreeString(0) + '\n'

def makeTree():
    root = BinaryTree(10)
    root.left = BinaryTree(5)
    root.left.left = BinaryTree(1)
    root.left.left.right = BinaryTree(4)
    root.right = BinaryTree(35)
    root.right.left = BinaryTree(15)
    root.right.right = BinaryTree(40)
    root.right.right.left = BinaryTree(37)

    return root

def main(tree):
    return tree.getSecondMax()

if __name__ == '__main__':
    tree = makeTree()
    print tree
    print main(tree)
