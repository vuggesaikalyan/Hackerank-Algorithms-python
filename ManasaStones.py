
T = int(input())

for _ in range(T):
    n = int(input())
    a = int(input())
    b = int(input())

    values = set()
    for t in range(0, n):
        v = t * a + (n - 1 - t) * b
        values.add(v)

    print(' '.join(map(str, sorted(list(values)))))