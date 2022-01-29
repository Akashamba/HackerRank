def weightedMean(X, W):
    w_mean = 0
    for i in range(len(X)):
        w_mean += X[i]*W[i]
    
    return round(w_mean/sum(W), 1)

X = [int(x) for x in input().split()]
W = [int(x) for x in input().split()]
print(weightedMean(X, W))
