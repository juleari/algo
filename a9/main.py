import re

def increment_in_string(str_):
    def inc_(matchobj):
        num_before = matchobj.group(0)
        num_after = `int(num_before) + 1`
        return num_after if len(num_before) == len(num_after) else num_after[1:]

    return re.sub('(\d+)', inc_, str_)

def main(str_):
    return increment_in_string(str_)

if __name__ == '__main__':
    print main('63872')
