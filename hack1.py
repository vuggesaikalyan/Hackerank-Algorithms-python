b = int(input())
n = int(input())
m = int(input())
l = []
k = []
u = []
for i in range(0, n):
    a = input()
    k.append(a)
for i in range(0, m):
    a1 = input()
    u.append(a1)
for i in range(0, n):
    for j in range(0, m):
        c = int(k[i]) + int(u[j])
        if c < b:
            l.append(c)
        else:
            if k[i]==k[n-1] and u[i]==u[m-1]:
                print(-1)
                exit()
l1 = sorted(l)
print(l1[len(l1) - 1])
