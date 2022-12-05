import numpy as np
from mpi4py import MPI
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
    
    comm = MPI.COMM_WORLD
    my_rank = comm.Get_rank()
    my_size = comm.Get_size()
    
    def f(x):
        return np.exp(-x)
    
    a = -2
    b = 2
    n = 10000000
    h = (b-a)/n
    
    local_n = n / my_size
    local_a = a + my_rank * local_n*h
    local_b = local_a + local_n*h
    dest = 0

    local_n = int(local_n)
    
    result = np.zeros(1)
    recv_sum = np.zeros(1)
    
    result[0] = Simpson13Rule(f, local_a, local_b, local_n)
    
    
    if my_rank == 0:
        total = result[0]
        
        for i in range(1, my_size):
            comm.Recv(recv_sum)
            total = total + recv_sum
    else:
        comm.Send(result[0], dest=0)
    
    if comm.rank == 0:
        print("The approximate integral via parallel Simpson's 1/3 Rule is:", round(total[0], 10))
        toc = time.time()
        print("The program took", round(toc-tic, 10), "seconds to execute")
    
    
    
    
    
    
    
    