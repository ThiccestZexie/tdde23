def choose(n, k): 
    if k > (n/2):
        k = n - k
    if k == 0 or n == 0:
        return 1
    else:
        return n * choose(n-1, k-1)//k

