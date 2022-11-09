import numpy as np

def main():
    N = 100

    A, B = make_arrays(N)
    C_np = numpy_dot(A, B)
    C_mn = manual_dot(A, B)

    print(C_np.size, C_mn.size)
    print(np.allclose(C_np, C_mn))

def make_arrays(N):
    A = np.random.rand(N,N)
    B = np.random.rand(N,N)
    return A, B

def numpy_dot(A, B):
    return A.dot(B)

def manual_dot(A, B):
    assert A.shape == B.shape
    N = A.shape[0]

    C = np.zeros((N,N))
    for i in range(N):
        for j in range(N):
            for k in range(N):
                C[i,j] += A[i,k] * B[k,j]
    return C

if __name__ == "__main__":
    main()


# python -m cProfile -o matmult.profile matmult.py
# pyprof2calltree -i matmult.profile -o callgrind.100
# qcachegrind callgrind.100
