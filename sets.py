def func():
 l=[]
 s=input('')
 for i in range(0,len(s)):
    for j in range(i+1,len(s)):
        if(s[i]==s[j]):
            length=j-i
            l.append(length)
            i=j
        elif():
            length=len(s)
            l.append(length)
 return max(l)
result=func()
print(result)
