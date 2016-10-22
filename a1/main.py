class BinaryTree(object):
    def __init__(self, value=None, left=None, right=None):
        self.left = left
        self.right = right
        self.value = value

    def getLeftSum(self, isLeft):
        sum = 0

        if self.left:
            sum += self.left.getLeftSum(True)

        if self.right:
            sum += self.right.getLeftSum(False)

        if isLeft and not(self.left) and not(self.right):
            return self.value

        return sum

    def getPartString(self, part, tab):
        noneStr = ' ' * tab + 'None'
        return noneStr if part == None else part.getTreeString(tab)

    def getTreeString(self, tab):
        nTab = tab + 2
        ftStr = ' ' * tab + '%s\n%s\n%s'
        return ftStr % (self.value,
                        self.getPartString(self.left, nTab),
                        self.getPartString(self.right, nTab))

    def __str__(self):
        return self.getTreeString(0)

    def __repr__(self):
        return '\n' + self.getTreeString(0) + '\n'

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
    return tree.getLeftSum(True)

if __name__ == '__main__':
    tree = makeTree()
    print tree
    print main(tree)
