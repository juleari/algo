import string

def roundTo(hex_floor, hex_ceil, hex_in):
    return hex_floor \
        if hex_in <= hexMath(hex_floor * 2, 8, '02X') \
        else hex_ceil

def hexMath(hex_in, hex_add, mask='01X'):
    return format((int(hex_in, 16) + hex_add), mask)

def roundHex(color_hex3):

    def countColor(i):
        hex_in = color_hex3[i:i+2]

        hex_in_1, hex_in_2 = hex_in

        return roundTo(hex_in_1, hexMath(hex_in_1, 1), hex_in) \
            if hex_in_2 > hex_in_1 \
            else roundTo(hexMath(hex_in_1, -1), hex_in_1, hex_in)

    rgb = [ countColor(i) for i in range(0, 6, 2) ]

    return string.join(rgb, '')

def main(color_hex3):
    return roundHex(color_hex3)

if __name__ == '__main__':
    print roundHex('F01121')
