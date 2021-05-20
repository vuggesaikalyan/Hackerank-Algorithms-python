n, k = map(int, input().split())
list = list(int(num) for num in input( ).strip().split())[:n]
def jessie(l,x):
   count=0
   while(min(l)<x):
       count=count+1
       l=sorted(l)
       b=l[0]*1+l[1]*2
       l.pop(0)
       l.pop(1)
       l.append(b)
       
   return count-1
print( jessie(list,k))
    
            

