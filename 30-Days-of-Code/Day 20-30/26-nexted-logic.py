# Enter your code here. Read input from STDIN. Print output to STDOUT
ad, am, ay = [int(x) for x in input().split()]
ed, em, ey = [int(x) for x in input().split()]


        
if ey>ay:
    print(0)
elif ey == ay:
    if em > am:
        print(0)
    elif em == am:
        if ed >= ad:
            print(0)
        else: print(15*(ad-ed))
    else: print(500*(am-em))
else: print(10000)
