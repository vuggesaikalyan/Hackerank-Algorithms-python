def minimumOperations(arr, n):
    s = 0
    for i in range(0, n):
        s += arr[i]
    if s % n != 0:
        return -1
    d_s = 0
    eq = s / n
    for i in range(0, n):
        d_s += abs(arr[i] - eq)

    return int(d_s / 2)


arr = [5, 3, 2, 6]
n = len(arr)
print(minimumOperations(arr, n))
