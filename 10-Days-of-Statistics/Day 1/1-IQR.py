#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'interQuartile' function below.
#
# The function accepts following parameters:
#  1. INTEGER_ARRAY values
#  2. INTEGER_ARRAY freqs
#

def median(arr):
    n = len(arr)
    if n%2==0:
        return (arr[n//2-1] + arr[n//2]) / 2
    return arr[n//2]
    
def interQuartile(values, freqs):
    # Print your answer to 1 decimal place within this function
    S = []
    for i in range(len(values)):
        for _ in range(freqs[i]):
            S.append(values[i])
    S.sort()
    n = len(S)
    
    q2 = median(S)
    if n%2 == 0:
        q1 = median(S[:n//2])
        q3 = median(S[n//2:])
    else: 
        q1 = median(S[:n//2])
        q3 = median(S[n//2+1:])
    
    print(round(float(q3-q1), 1))

if __name__ == '__main__':
    n = int(input().strip())

    val = list(map(int, input().rstrip().split()))

    freq = list(map(int, input().rstrip().split()))

    interQuartile(val, freq)
