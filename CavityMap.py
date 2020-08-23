import os
def cavityMap(grid):
    v = []
    for i, v in enumerate(grid[1:-1], 1):
        for x, j in enumerate(v[1:-1], 1):
            m = j
            if m > v[x - 1] and m > v[x + 1] and m > grid[i - 1][x] and m > grid[i + 1][x]:
                v = v[:x] + 'X' + v[x + 1:len(v)]
        grid[i] = v
    return grid


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    grid = []

    for _ in range(n):
        grid_item = input()
        grid.append(grid_item)

    result = cavityMap(grid)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()