import numpy as np
import time

def Bisection(f, a, b, tol):
    
    if f(a) * f(b) >= 0:
        raise("There are no roots within the interval")
        
    error = 100
    c0 = 0
    
    while (error > tol):
        c1 = (a + b) / 2
        if f(a) * f(c1) < 0:
            b = c1
        else:
            a = c1
            
        error = abs((c1 - c0) / c1)
        c0 = c1
        
    return c1

if __name__ == "__main__":
    
    tic = time.time()
    
    def f(x):
        return x**2 - 2
    
    a = 0
    b = 2
    tol = 1e-10
    
    result = Bisection(f, a, b, tol)
    
    toc = time.time()
    
    print("The approximate root according via Bisection method is:", round(result, 10))
    print("The program took:", round(toc-tic, 10), "seconds to execute")