import numpy as np
from mpi4py import MPI
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
    
    comm = MPI.COMM_WORLD
    my_rank = comm.Get_rank()
    my_size = comm.Get_size()
    
    def f(x):
        return x**2 - 2

    def df(x):
        return 2*x
    
    x0 = 1
    tol = 1e-15
    
    result = np.zeros(1)
    recv = np.zeros(1)

    result[0] = Newton_Raphson(f, df, x0, tol)
    
    if my_rank == 0:
        root = result[0]
        
        for i in range(1, my_size):
            comm.Recv(recv)
    else:
        comm.Send(result[0], dest=0)
    
    if comm.rank == 0:
        print("The approximate root via parallel Newton-Raphson method is:", round(root, 10))
        toc = time.time()
        print("The program took", round(toc-tic, 10), "seconds to execute")
    
    

    

