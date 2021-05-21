def minion_game(s):
    n=len(s)
    l=[]
    countv=0
    countc=0
    for i in range(0,n):  
      for j in range(i,n):  
        l.append(s[i:(j+1)]);
    v=['A','E','I','O','U']
    for i in range(len(l)):
      s1=l[i]
      if s1[0] in v:
         countv=countv+1
      else:
         countc=countc+1
    if countv>countc:
      print("Kevin",countv)
    if countv==countc:
        print("Draw")
    else:
      print("Stuart",countc)

if __name__ == '__main__':
    s = input()
    minion_game(s)