def f(i, N):
    if i == N:
        for j in range(N):
            if bit[j]:
                print(A[j], end=' ')
        print()
    else:
        bit[i] = 1
        f(i+1, N)
        bit[i] = 0
        f(i+1, N)

A = [1,2,3]
N = len(A)
bit = [0]*N

f(0,3)
