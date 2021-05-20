def alphanum(s):
 count=0
 for i in range(len(s)):
    if s[i].isalnum():
        count=count+1
        print("True")
        break
 if count==0:
     print("False")
def alpha(s):
 count=0
 for i in range(len(s)):
    if s[i].isalpha():
        count=count+1
        print("True")
        break
 if count==0:
     print("False")
def digit(s):
 count=0
 for i in range(len(s)):
    if s[i].isdigit():
        count=count+1
        print("True")
        break
 if count==0:
     print("False")
def lower(s):
 count=0
 for i in range(len(s)):
    if s[i].islower():
        count=count+1
        print("True")
        break
 if count==0:
     print("False")
def upper(s):
 count=0
 for i in range(len(s)):
    if s[i].isupper():
        count=count+1
        print("True")
        break
 if count==0:
     print("False")
str=input("")
alphanum(str)
alpha(str)
digit(str)
lower(str)
upper(str)
    