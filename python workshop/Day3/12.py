#used in networking or data orienting or to track functions time measure save it def time measure

import time

def tm(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(end - start)
        return result
    return wrapper
#appoch in time.time new york time is there

@tm
def sum(n):
    if n <= 1:
        return 1
    
    return n + sum(n-1)
print(sum(10))