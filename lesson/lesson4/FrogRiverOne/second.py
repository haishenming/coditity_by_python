
import random

li = [random.randint(1, 4) for i in range(1000000)]
li.append(5)
test_data = (5, li)


test_data = (5, [1, 3, 1, 4, 2, 3, 5, 4])


# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(X, A):
    # write your code in Python 3.6
    locals = [i for i in range(1, X+1)]
    set_locals = set(locals)
    if set(A) != set_locals:
        # 树叶不全，必不能铺满
        return -1

    lenght = len(A)
    has_lenght = 0
    for i in range(lenght):
        A.pop()
        has_lenght += 1
        if set(A) != set_locals:
            # 树叶不全，必不能铺满
            return lenght - has_lenght


    return -1


if __name__ == '__main__':
    print(solution(*test_data))
