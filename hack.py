dic={}
for i in range(1,6):
    n=input()
    s=input()
    dic[n]=s
dict1 = sorted(dic)
dict1.pop(4)
if dict1[3]==dict1[2]:
    for i, j in dict1.items():
        sorted_dict1 ={i:sorted(j)}
        print(sorted_dict1[3])
        print(sorted_dict1[2])
elif():
    print(dic1[3])




