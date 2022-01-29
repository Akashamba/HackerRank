#!/bin/python3

import math
import os
import random
import re
import sys

def binary(x):
    bin_rep = ""
    while x > 0:
        bin_rep = str(x%2) + bin_rep
        x //= 2
    return bin_rep

def count(string):
    max_count = 0
    for i in range(len(string)):
        current = string[i]
        count = 0
        while i<len(string) and string[i] == current:
            count += 1
            i += 1
            
        if max_count < count: max_count = count
        
    return max_count
            
    
if __name__ == '__main__':
    n = int(input().strip())
    bin_rep = binary(n)
    print(count(bin_rep))
