#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))
    swap = 0
    # Write your code here
    for i in range(len(a)):
        nswap = 0
        for j in range(len(a)-1):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
                nswap+=1
        swap += nswap       
        if nswap == 0: break
        

print(f"Array is sorted in {swap} swaps.")
print(f"First Element: {a[0]}")
print(f"Last Element: {a[-1]}")
