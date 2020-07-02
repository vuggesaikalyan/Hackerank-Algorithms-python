def median(num1,num2):
    num=num1+num2
    final=sorted(num)
    if(len(num)%2==0):
        mid1=len(num)/2
        mid2=mid1+1
        print(num(mid1),num(mid1))
    elif(len(num)%2==1):
        mid=(len(num)+1)/2
        print(num(mid))
result=median((1,2,3,4),(6,7,8,9))
print(result)

