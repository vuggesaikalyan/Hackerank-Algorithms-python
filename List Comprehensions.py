x=int(input())
y=int(input())
z=int(input())
n=int(input())
ans = [];
a = [];
for X in range(x+1):
    for Y in range(y+1):
        for Z in range(z+1):
          if X+Y+Z != n:
                a = [X,Y,Z];
                ans.append(a);
print(ans);
