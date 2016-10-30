class ScalarHelper(object):
    def __init__(self, xs, ys):
        self.xs = xs
        self.ys = ys

        self._yn = len(ys)

        self._j = -1
        self._get_next_y()

        self._scalar = 0

    def _get_next_y(self):
        self._j += 1
        if self._j < self._yn:
            y = self.ys[self._j]
            self.y_value = y[0]
            self.y_count = y[1]
        else:
            self.y_count = 0

    def calc(self):
        for x in self.xs:
            self.x_value = x[0]
            self.x_count = x[1]

            while self.y_count < self.x_count:
                self._scalar += self.x_value * self.y_value * self.y_count
                self.x_count -= self.y_count
                self._get_next_y()

            if self.x_count:
                if self.y_count == self.x_count:
                    self._scalar += self.x_value * self.y_value * self.y_count
                    self._get_next_y()
                else:
                    self._scalar += self.x_value * self.y_value * self.x_count
                    self.y_count -= self.x_count

        return self._scalar

def main(xs, ys):
    return ScalarHelper(xs, ys).calc()

if __name__ == '__main__':
    print main([(2, 4), (3, 3)], [(4, 2), (5, 5)])
