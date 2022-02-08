#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    N = int(input().strip())
    result = []
    for N_itr in range(N):
        firstName, emailID = input().rstrip().split()
        
        if re.search(".@gmail.com", emailID):
            result.append(firstName)

    result.sort()
    print(*result, sep="\n")
