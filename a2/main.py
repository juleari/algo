def rotate(A):
    n = len(A)
    n1 = n - 1
    n2 = int( (n + 1) / 2 )

    for i in range(n2):
        for j in range(i, n1 - i):
            t = A[i][j]
            ii, jj = i, j
            for k in range(3):
                A[ii][jj] = A[n1 - jj][ii]
                ii, jj = n1 - jj, ii
            A[j][n1 - i] = t

    return A

def printA(A):
    for i in range(len(A)):
        print A[i]

def main(A):
    return rotate(A)

if __name__ == '__main__':
    A = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]

    printA( A )
    printA( main(A) )
