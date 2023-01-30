T = int(input())

for _ in range(T):
    k, n = int(input()),int(input())

    floor = [i+1 for i in range(n)]
    for stage in range(k):
        floor = []