'''
5
55 7 78 12 42
'''

arr = [55, 7, 78, 12, 42]
N = 5

def bubblesort(N,arr):
    for i in range(N-1, 0, -1):  # 각 구간의 끝
        for j in range(i):  # 비교할 왼쪽 원소
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]  # 큰 원소 오른쪽으로
    return arr

print(bubblesort(N, arr))

