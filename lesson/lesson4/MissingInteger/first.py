# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

test_data = [1, 3, 6, 2, 1, 4]


def solution(A):
    # write your code in Python 3.6
    A = sorted(A)

    for i, a in enumerate(A, 1):
        try:
            a_plus = A[i]
        except:
            if a + 1 > 0:
                return a + 1
            else:
                return 1
        if a + 1 != a_plus and a != a_plus:
            if a + 1 > 0:
                return a + 1


if __name__ == '__main__':
    print(solution(test_data))
