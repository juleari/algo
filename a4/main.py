class MaxSumHelper(object):
    def __init__(self, xs):
        self.xs = xs

    def _set_new_cur_sum(self, i):
        x = self.xs[i]

        self._cur_sum = x
        self._max_elem = x
        self._min_elem = x
        self._min2_elem = None

        self._cur_index_start = i
        self._cur_index_end = i

    def _set_new_max_sum(self):
        self._max_sum = self._cur_sum
        self._max_index_start = self._cur_index_start
        self._max_index_end = self._cur_index_end

    def _check_condition(self):
        return self._max_elem <= self._min_elem + self._min2_elem

    def _update_cur_sum(self, i):
        x = self.xs[i]

        self._cur_sum += x
        self._cur_index_end = i

    def _update_sums(self, i):
        if self._check_condition():
            self._update_cur_sum(i)

        else:
            if self._cur_sum > self._max_sum:
                self._set_new_max_sum()

            self._set_new_cur_sum(i)

    def _calc_new_sums(self, i):
        x = self.xs[i]

        if x >= self._max_elem:

            if self._min2_elem == None:
                self._min2_elem = self._max_elem

            self._max_elem = x

        elif x <= self._min_elem:
            self._min2_elem, self._min_elem = self._min_elem, x

        elif x < self._min2_elem or self._min2_elem == None:
            self._min2_elem = x

        self._update_sums(i)

    def _calc_line(self, index_init, range_list):
        self._set_new_cur_sum(index_init)
        self._set_new_max_sum()

        for i in apply(range, range_list):
            self._calc_new_sums(i)

        if self._cur_sum > self._max_sum:
            self._set_new_max_sum()

    def _get_max_sum(self):
        step = cmp(self._max_index_end, self._max_index_start)
        self._max_index_end += step

        return [self.xs[self._max_index_start]] if step == 0\
            else self.xs[self._max_index_start:self._max_index_end:step][::step]

    def max_sum_xs(self):
        len_xs = len(self.xs)

        if len_xs == 0:
            return []

        self._calc_line(0, (1, len_xs))
        self._calc_line(-1, (-1, -(len_xs + 1), -1))

        return self._get_max_sum()

def main(xs):
    return MaxSumHelper(xs).max_sum_xs()

if __name__ == '__main__':
    print main([8, 10, -5, 20, -27, 30])
