def zeroEnd_py(A):
    return [ a for a in A if a != 0 ] + [ a for a in A if a == 0 ]

def zeroEnd(A):

    n = len(A)
    j = 0

    for i in range(n):
        if A[i] != 0:
            A[i - j] = A[i]
        else:
            j += 1

    for i in range(n - j, n):
        A[i] = 0

    return A

def main(A):
    return zeroEnd(A)

if __name__ == '__main__':
    print zeroEnd([8, 9, 0, 3, 0, 4, 5])
    print zeroEnd_py([8, 9, 0, 3, 0, 4, 5])
