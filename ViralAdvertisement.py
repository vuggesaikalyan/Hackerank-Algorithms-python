n=int(input())
s=5
cum=2
for i in range(1,n):
        s=(s//2)*3
        l=s//2
        cum=cum+l
print(cum)
