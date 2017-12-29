
import random

li = [random.randint(1, 4) for i in range(1000000)]
li.append(5)
test_data = (5, li)


# test_data = (5, [1, 3, 1, 4, 2, 3, 5, 4])


# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(X, A):
    # write your code in Python 3.6

    pass




if __name__ == '__main__':
    print(solution(*test_data))
