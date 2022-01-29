def median(arr, n):
    if n%2==0:
        return int((arr[n//2-1] + arr[n//2]) / 2)
    return arr[n//2]

def quartiles(arr):
    # Write your code here
    arr.sort()
    n = len(arr)
    
    q2 = median(arr, n)
    q1 = median(arr[:n//2], n//2)
    
    if n%2 == 0:
        q3 = median(arr[n//2:], n//2)
    else:
        q3 = median(arr[n//2+1:], n//2)
    
    return [q1, q2, q3]

 arr = [int(x) for x in input().split()]
print(quartiles(arr))
