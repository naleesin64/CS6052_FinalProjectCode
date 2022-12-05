import numpy as np
import time

def Newton_Raphson(f, df, x0, tol):
    i = 0
    eps = 1

    while (eps > tol):
        x1 = x0 - (f(x0) / df(x0))
        i = i+1

        if (abs(x1 - x0) < tol):
            break
        else:
            x0 = x1

    return x1

if __name__ == "__main__":
    
    tic = time.time()
    
    def f(x):
        return x**2 - 2

    def df(x):
        return 2*x
    
    x0 = 1
    tol = 1e-15
    
    result = Newton_Raphson(f, df, x0, tol)
    
    toc = time.time()
    
    print("The approximate root via Newton-Raphson method is:", round(result, 10))
    print("The program took:", round(toc-tic, 10), "seconds to execute")
    
    