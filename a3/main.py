class Stack(object):
    def __init__(self):
        self.stack = []
        self.stackMax = []

    def push(self, x):
        self.stack.append(x)
        if x >= self.max():
            self.stackMax.append(x)

    def pop(self):
        x = self.stack.pop()
        if x == self.max():
            self.stackMax.pop()

        return x

    def max(self):
        return None if len(self.stackMax) == 0 else self.stackMax[-1]

def main(input):
    s = Stack()

    for x in input:
        if x == '-':
            s.pop()
        elif x == '>':
            return s.max()
        else:
            s.push(x)

if __name__ == '__main__':
    print main([5, 3, 6, 2, '>'])
