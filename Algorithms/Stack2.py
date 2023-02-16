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

A = [1,2,3,4]
N = len(A)
bit = [0]*N

f(0,N)



P = [1,2,3,4]
N = len(P)

def f(i, k):
    if i == k:
        print(P)
    else:    
        for j in range(i, k):
            P[i], P[j] = P[j], P[i]
            f(i+1, k)
            P[i], P[j] = P[j], P[i]

f(0, N)