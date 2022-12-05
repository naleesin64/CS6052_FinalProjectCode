import numpy as np
from mpi4py import MPI
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
    
    comm = MPI.COMM_WORLD
    my_rank = comm.Get_rank()
    my_size = comm.Get_size()
    
    
    def f(x):
        return x**2 - 2
    
    a = 0
    b = 2
    tol = 1e-10
    
    local_a = a
    local_b = b
    
    dest = 0
    
    result = np.zeros(1)
    recv = np.zeros(1)
    
    result[0] = Bisection(f, local_a, local_b, tol)
    
    if my_rank == 0:
        root = result[0]
        
        for i in range(1, my_size):
            comm.Recv(recv)
    else:
        comm.Send(result[0], dest=0)
    
    if comm.rank == 0:
        print("The approximate root via parallel Bisection method is:", round(root, 10))
        toc = time.time()
        print("The program took", round(toc-tic, 10), "seconds to execute")
    
