n=int(input())
b=[]
list=[]
def total(l,b):
    if len(l)!=10:
        c="invalid"
        b.append(c)
def Counter(str,b):
	upper,number, special = 0, 0, 0
	for i in range(len(str)):
		if str[i].isupper():
			upper += 1
		elif str[i].isdigit():
			number += 1
		else:
			special += 1
    if upper<2:
        c="invalid"
        b.append(c)
    if number<3:
        c="invalid"
        b.append(c)
    if special>0:
        c="invalid"
        b.append(c)
def noRepeat(stri,b):
     set1=set(stri) 
     len1=len(stri)
     len2=len(set1)
     if len1 != len1:
         c="invalid"
         b.append(c)
for i in range(n):
    s=input("")
    list.append(s)
for i in range(n):
   total(list[i],b)
   s=""
   s=s.join(list[i])
   Counter(s,b)
   noRepeat(s,b)
 
if b[0]=="invalid":
    print("invalid")
else:
    print("valid")

   

