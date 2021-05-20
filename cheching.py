l=["pizza","puff","cooldrink"]
s=[]
for i in range(len(l)):
    s1=l[i]
    print("enter the number of " +s1+" bought:",end='')
    v=int(input())
    s.append(v)
print("Bill details:")
for i in range(len(l)):
    s2=l[i]
    print("number of " +s2+":",s[i])
ans=s[0]*100+s[1]*20+s[2]*10
print("total bill =",ans)