def stdDev(arr):
    # Print your answers to 1 decimal place within this function
    mean = sum(arr)/len(arr)
    sum_distance = [x-mean for x in arr]
    sq_distance = [x**2 for x in sum_distance]
    stdDev = math.sqrt(sum(sq_distance)/len(sq_distance))
    
    return stdDev

arr = [int(x) for x in input().split()]
print(stdDev(arr))
