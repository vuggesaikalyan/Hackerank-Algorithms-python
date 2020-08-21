n=int(input())
s=input("")
l=len(s)
count=0
valley=0
for i in range(l):
    if s[i] == 'U':
        count=count+1
    if s[i] == 'D':
        count=count-1
    if count == 0:
        valley=valley+1
print(valley-1)

