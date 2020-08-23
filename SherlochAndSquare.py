import math


def squaresBetween(a, b):
    count = math.floor(math.sqrt(b)) - math.floor(math.sqrt(a - 1))
    return count


if __name__ == '__main__':
    test_count = int(input())

    for _ in range(test_count):
        a, b = tuple(int(pair) for pair in input().split())
        print(squaresBetween(a,b))
