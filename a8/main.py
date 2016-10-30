def deshifr(str_after_shifr):
    str_before_shifr = ''

    for s in str_after_shifr:
        str_before_shifr = str_before_shifr + s \
            if not len(str_before_shifr) or s != str_before_shifr[-1] \
            else str_before_shifr[0:-1]

    return str_before_shifr

def main(shifr):
    return deshifr(shifr)

if __name__ == '__main__':
    print main('wwstdaadierfflitzzz')
