import numpy as np
import time

def Simpson13Rule(f, a, b, n):
    h = (b-a)/n
    
    total_sum = (h/3) * (f(a) + f(b))
    x1 = a + h
    
    for i in range(1,n):
        if i % 2 == 0:
            total_sum += 2 * h / 3 * f(x1)
        else:
            total_sum += 4 * h / 3 * f(x1)
        x1 = x1 + h
    
    return total_sum

if __name__ == "__main__":
    
    tic = time.time()
    
    def f(x):
        return np.exp(-x)
    
    a = -2
    b = 2
    n = 10000000
    
    result = Simpson13Rule(f, a, b, n)
    
    toc = time.time()
    
    print("The approximate integral via Simpson's 1/3 Rule is:", round(result, 10))
    print("The program took:", round(toc-tic, 10), "seconds to execute")