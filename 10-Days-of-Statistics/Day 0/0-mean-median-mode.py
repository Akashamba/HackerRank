def mean(arr):
    return round(float(sum(arr)/len(arr)), 1)

def median(arr, n):
    if n%2 == 0:
        return round((arr[n//2-1]+arr[n//2])/2, 2)
    else: return round(arr[n//2], 1)
        
def mode(arr, n):
    count = {}

    for i in range(n):
        try:
            count[arr[i]] += 1
        except: count[arr[i]] = 1

    mode = arr[0]
    for ele in count.keys():
        if count[mode] < count[ele]:
            mode = ele
    
    return mode
            

n = int(input())
arr = [int(x) for x in input().split()]
arr.sort()

print(mean(arr))
print(median(arr, n))
print(mode(arr, n))
