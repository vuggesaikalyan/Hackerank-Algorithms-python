i=int(input())
j=int(input())
k=int(input())
count=0
for a in range(i,j+1):
    Reverse = 0
    while a > 0:
        Reminder = a % 10
        Reverse = (Reverse * 10) + Reminder
        a = a // 10
    diff=a-Reverse
    if diff == 0:
        count=count+1
    if diff%k == 0:
        count=count+1
print(count)