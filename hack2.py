n = int(input())
l = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W',
     'X', 'Y', 'Z']
for i in range(1, n + 1):
    for k in range(0, i ):
        print(l[k], end='')

        for y in range(1,k+1):
            print(l[y], end='')

    print()
