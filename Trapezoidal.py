import numpy as np
import time

def trapezoid(f, a, b, n):
    h = (b-a)/n
    
    x1 = (f(a) + f(b)) / 2
    
    for i in range(1,n):
        x1 = x1 + f(a + i*h)
        
    return x1 * h


if __name__ == "__main__":
    
    tic = time.time()
    
    def f(x):
        return np.exp(-x)
    
    a = -2
    b = 2
    n = 10000000
    
    result = trapezoid(f, a, b, n)
    
    toc = time.time()
    
    print("The approximate integral via Trapezoidal Rule is:", round(result, 10))
    print("The program took:", round(toc-tic, 10), "seconds to execute")
    