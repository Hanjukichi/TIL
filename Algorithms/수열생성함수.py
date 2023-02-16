NMAX = 10
MAXCANDIDATES = 10


# 남아있는 candidate를 만드는 함수
# a == 현재 만드는 순열, k == 순열의 다음 칸,
# input = 만들고자 하는 순열의 크기
# candidates == 다음에 올 후보들이 저장될 리스트
def construct_candidate(a, k, input, candidate):
    # 순열에 사용된 적 있는지 검증
    in_perm = [False] * NMAX

    # a를 검사하며 사용됐는지 판단
    for i in range(1, k):
        in_perm[a[i]] = True

    # 후보 갯수
    ncandidate = 0
    # 1부터 만들고자 하는 순열 크기까지 순회
    for i in range(1, input + 1):
        if not in_perm[i]:
            candidate[ncandidate] = i
            ncandidate += 1
    return ncandidate


# 실제로 순열을 만드는 함수
# a == 현재 만드는 순열, k == 순열의 다음 칸,
# input = 만들고자 하는 순열의 크기


def backtrack(a, k, input):
    global MAXCANDIDATES
    candidate = [0] * max(arr)

    if k == input:
        print(a)
    else:
        k += 1
        ncandidates = construct_candidate(a, k, input, candidate)
        for i in range(ncandidates):
            a[k] = candidate[i]
            backtrack(a,k,input)

arr = [1,2,3,4]

backtrack(arr, 0, 4)