#!/bin/python3

import math
import os
import random
import re
import sys

def getsum(arr, row, col):
    result = sum(arr[row][col:col+3]) + arr[row+1][col+1] + sum(arr[row+2][col:col+3])
    return result
    
if __name__ == '__main__':

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))
        
        
    result = []
    for i in range(4):
       for j in range(4):
            result.append(getsum(arr, i, j))
            
    print(max(result))
    
