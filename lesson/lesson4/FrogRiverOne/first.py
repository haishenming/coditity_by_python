
test_data = (5, [1, 3, 1, 4, 2, 3, 5, 4])


# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(X, A):
    # write your code in Python 3.6
    locals = [i for i in range(1, X+1)]
    for i, a in enumerate(A):
        if a in locals:
            locals.pop(locals.index(a))
        if locals == []:
            return i
    return -1


if __name__ == '__main__':
    print(solution(*test_data))
