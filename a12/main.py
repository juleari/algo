def countMax(n, B, P):

    if n < 2:
        return 0

    max_sums = [0] * n

    for i in range(n):
        p = P[i] - 1
        delta = B[p]

        for j in range(p, n):
            if B[j] == 0:
                break
            B[j] -= delta

        max_sums[i] = max(B)

    return max_sums

def precount(n, A):
    B = [0] * n
    B[0] = A[0]

    for i in range(1, n):
        B[i] = A[i] + B[i - 1]

    return B

def main(n, A, P):
    return countMax(n, precount(n, A), P)

if __name__ == '__main__':
    import string
    n = int(input())

    A = map(int, raw_input().split())
    P = map(int, raw_input().split())

    B = precount(n, A)

    print B

    # B = [0] * n
    # P = [0] * n
    # B[0] = int(input())
    # for i in range(1, n):
    #     B[i] = B[i - 1] + int(input())
    #
    # for i in range(n):
    #     P[i] = int(input())

    print string.join(map(lambda x: '%s\n' % x, countMax(n, B, P)), '')
