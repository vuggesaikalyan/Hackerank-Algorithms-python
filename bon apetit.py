#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the bonAppetit function below.
def bonAppetit(bill, k, b):
    if b==sum(bill)/2:
        x=int(bill[k]/2)
        print(x)
    else:
        print("Bon Appetit")

if __name__ == '__main__':
    nk = input().rstrip().split()

    n = int(nk[0])

    k = int(nk[1])

    bill = list(map(int, input().rstrip().split()))

    b = int(input().strip())

    bonAppetit(bill, k, b)
