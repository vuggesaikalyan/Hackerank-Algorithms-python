n=int(input())
s=str(n)
sum=0
for i in range(len(s)):
    fact=1
    x=int(s[i])
    for j in range(1,x+1):
        fact=fact*j
    sum=sum+fact
if sum==n:
    print("yes")
else:
    print("NO")
