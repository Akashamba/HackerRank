# Enter your code here. Read input from STDIN. Print output to STDOUT
import math

t = int(input())

for _ in range(t):
    n = int(input())
    flag = True

    for i in range(1, int(math.sqrt(n))+1):
        if i!=1 and i!=n and n%i == 0:
            flag = False
            break

    if flag and n!=1: print("Prime")
    else: print("Not prime")
