#!/bin/python3

import math
import os
import random
import re
import sys



def pickingNumbers(a):
    a1=sorted(a)
    l=[]
    for i in range(0,n):
        count=1
        for j in range(i+1,n):
            if abs(a1[i]-a1[j])<=1:
                count=count+1
        l.append(count)
    return max(l)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = pickingNumbers(a)

    fptr.write(str(result) + '\n')

    fptr.close()
