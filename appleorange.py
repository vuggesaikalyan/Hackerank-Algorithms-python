#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countApplesAndOranges function below.
def countApplesAndOranges(s, t, a, b, apples, oranges):
    acount,bcount=0,0
    for i in range(0,len(apples)):
        if a+apples[i]>=s and a+apples[i]<=t:
            acount=acount+1
    for i in range(len(oranges)):
        if b+oranges[i]<=t and b+oranges[i]>=s:
            bcount=bcount+1
    print(acount)
    print(bcount)

if __name__ == '__main__':
    st = input().split()

    s = int(st[0])

    t = int(st[1])

    ab = input().split()

    a = int(ab[0])

    b = int(ab[1])

    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)
