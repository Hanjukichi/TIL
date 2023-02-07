# <b>배열2</b>
<br><br>

## <b>Ⅰ. 2차원 배열 </b>

---

### <b>ⅰ. 2차원 배열의 선언</b>
<br>

1차원 List를 묶어높은 List  

2원 이상의 다차원 list는 차원에 따라 index를 선언  

2차원 list의 선언: 세로 길이(행이 개수), 가로 길이(열의 개수)를 필요로 함  

python에서는 데이터 초기화를 통해 변수 선언과 초기화가 가능함

>```python
> arr = [[0,1,2,3],[4,5,6,7]]
>```  

---

### <b>ⅱ. 2차원 배열의 접근</b>
<br>

<b>배열 순회</b>  
n * m 배열의 n*m개의 모든 원소를 빠짐없이 조사하는 방법  

<b>행 우선 순회</b>
>```python
>for row in range(n):
>   for col in range(m):
>       Array[row][col]
>```  

<b>열 우선 순회</b>
>```python
>for col in range(n):
>   for row in range(m):
>       Array[row][col]
>```  

<b>지그재그 순회</b>
>```python
>for col in range(n):
>   for row in range(m):
>       Array[row][col + (m-1-2*col)*(row % 2)]
>```  

---

### <b>ⅲ. 2차원 배열의 상하좌우 탐색</b>
<br>

>```python
>drow = [0, 1, 0, -1]
>dcol = [1, 0, -1, 0]
>for row in range(n):
>   for col in range(m):
>       for d in range(4):
>           nr = row + drow[d]
>           nc = col + dcol[d]
>           if 0 <= nr < N and 0 <= nc < N
> test(arr[nr][nc])
>```  

---

### <b>ⅳ. 전치행렬</b>
<br>

>```python
>arr = [[1,2,3],[4,5,6],[7,8,9]]
>
>for r in range(3):
>   for c in range(3):
>       if r > c:
>           arr[r][c], arr[c][r] = arr[c][r], arr[r][c]
>
>
>```  

<br><br>


## <b>Ⅱ. 부분집합</b>

---

### <b>ⅰ. 부분 집합 생성</b>
<br>

완전 검색 기법으로 부분집합 합 문제를 풀기 위해서는  
우선 집합의 모든 부분집합을 생성한 후에 각 부분집합의 합을 계산해야함  

<b>부분집합의 수</b>  
집합의 원소가 n개 이면 부분집합의 수는 2^n
>```python
>a = [1,2,3,4]  # 2*2*2*2 = 16
>
>for i in range(2):
>   bit = [0,0,0,0]
>   bit[0] = i
>       for j in range(2):
>           bit[1] = j
>           for k in range(2):
>               bit[2] = k
>               for l in range(2):
>                   bit[3] = l  
>                   subset = []
>                   for m in range(4):
>                       if bit[m]:
>                           subset.append(a[m])
>                   print(subset)                   
>```  

---

### <b>ⅱ. 비트 연산자</b>
<br>

<b>&</b> : 비트 단위로 AND 연산을 한다.  
<b>|</b> : 비트 단위로 OR 연산을 한다.  
<b><<</b> : 피연산자의 비트 열을 왼쪽으로 이동한다.  
<b>>></b> : 피연산자의 비트 열을 오른쪽으로 이동한다.  

<b><< 연산자</b>  
2^n 즉, 원소 n개의 모든 부분 집합 개수를 뜻함  

<b>i&(1<<j)</b>  
i의 j번째 비트가 1인지 아닌지를 검사

---

### <b>ⅲ. 간결한 부분집합 생성</b>
<br>

>```python
>arr = [3,6,7,1,5,4]
>
>n = len(arr)
>
>for i in range(1<<n):
>   for j in range(n):
>       if i & (1<<j):
>           print(arr[j],end=", ")
>   print()
>print()
>```  

<br><br>


## <b>Ⅲ. 검색</b>

---

### <b>ⅰ. 검색이란?</b>
<br>

저장되어 있는 자료 중에서 원하는 항목을 찾는 작업  

목적하는 탐색 키를 가진 항목을 찾는 것
- 탐색 키(search key) : 자료를 구별하여 인식할 수 있는 키  

검색의 종류
- 순차 검색(sequential search)
- 이진 검색(binary search)
- 해쉬(hash)

---

### <b>ⅱ. 순차 검색(sequential search)</b>
<br>

일렬로 되어 있는 자료를 순서대로 검색하는 방법
- 가장 간단하고 직관적인 검색 방법
- 순차구조로 구현된 자료 구조에서 원하는 항목을 찾을 때 유용함
- 구현이 쉽지만, 검색 대상의 수가 많은 경우에는 수행시간이 급격히 증가하여 비효율적  

2가지 경우
- 정렬되어 있지 않은 경우
- 정렬되어 있는 경우

---

### <b>ⅲ. 정렬되어 있지 않은 경우</b>
<br>

<b>검색 과정</b>
- 첫 번째 원소부터 순서대로 검색 대상과 키 값이 같은 원소가 있는지 비교
- 동일한 원소를 찾으면 그 원소의 인덱스를 반환
- 자료 구조의 마지막에 이를 때까지 검색 대상을 찾지 못하면 검색 실패  

찾고자 하는 원소의 순서에 따라 비교회수가 결정됨
- n번째 원소를 찾을 때는 n번 비교  

정렬되지 않은 자료에서의 순차 검색의 평균 비교 회수
- (n+1)/2  

시간 복잡도:
- O(n)

구현 예
>```python
>def sequentialSearch(a, n, key):
>   i = 0
>   while i < n and a[i] != key:
>       i += 1
>   if i < n: 
>        return i
>   else: 
>        return -1
>```  

---

### <b>ⅳ. 정렬되어 있는 경우</b>
<br>

<b>검색 과정</b>
- 오름차순 정렬 가정
- 자료를 순차적으로 검색하면서 키값을 비교
- 원소의 키 값이 검색 대상의 키값보다 크면 검색 종료

찾고자 하는 원소의 순서에 따라 비교회수가 결정됨
- 검색 실패 반환의 경우 평균 비교 횟수가 반토막 

시간 복잡도:
- O(n)

구현 예
>```python
>def sequentialSearch(a, n, key):
>   i = 0
>   while i < n and a[i] < key:
>       i += 1
>   if i < n and a[i] == key: 
>        return i
>   else: 
>        return -1
>```  

---

### <b>ⅴ. 이진 검색(Binary Search)</b>
<br>

자료의 가운데에 있는 항목과 비교 후 다음 검색의 위치 결정  

목적 키를 찾을 때까지 검색 범위를 반으로 줄여감  

이진 검색을 위해선 자료가 정렬되어 있어야 함

<b>검색 과정</b>
- 자료의 중앙에 있는 원소 선택
- 중앙 원소의 값과 찾고자 하는 목표값 비교
- 중앙 원소보다 작으면 왼쪽 반에서 새로 검색, 크면 오른쪽 반에서 새로 검색
- 찾을 때까지 반복  

<b>구현</b>  
- 검색 범위의 시작점과 종료점을 이용하여 검색을 반복 수행
- 자료에 삽입이나 삭제가 발생했을 때 배열의 상태를 항상 정렬 상태로 유지 필요

>```python
>def binarysearch(a, n, key):
>   start = 0
>   end = n-1
>   while start <= end:
>       middle = (start + end) // 2
>       if a[middle] == key:
>           return middle
>       elif a[middle] > key:
>           end = middle - 1
>       else:
>           start = middle + 1
>   return False
>```

<b>재귀함수 이용</b> 
>```python
>def binarysearch(a, n, key):
>   start = 0
>   end = n-1
>   while start <= end:
>       middle = (start + end) // 2
>       if a[middle] == key:
>           return middle
>       elif a[middle] > key:
>           end = middle - 1
>       else:
>           start = middle + 1
>   return False
>```

<br><br>


## <b>Ⅳ. 인덱스</b>

---

### <b>ⅰ. 인덱스란?</b>
<br>

테이블에 대한 동작 속도를 높여주는 자료 구조를 일컫음  

인덱스를 저장에 필요한 디스크 공간은 보통 테이블을 저장하는데 필요한 공간보다 작다.  

보통 인덱스는 키-필드만 갖고 있고, 테이블의 다른 세부 항목들은 갖고 있지 않기 때문  

배열을 사용한 인덱스
- 대량의 데이터를 매번 정려하면, 프로그램 반응은 느려짐
- 대량 데이터의 성능 저하 문제를 해결하기 위해 배열 인덱스 사용

---

### <b>ⅱ. 선택 정렬(Selection Sort)</b>
<br>

주어진 자료들 중 가장 작은 값의 원소부터 차례대로 선택하여 위치를 교환하는 방식  

<b>정렬과정</b>
- 주어진 리스트 중에서 최소값을 찾는다.
- 그 값을 리스트의 맨 앞에 위치한 값과 교환
- 맨 처음 위치를 제외한 나머지 리스트를 대상으로 반복  

시간 복잡도
- O(n^2)  

알고리즘
>```python
>def selection_sort(a, n):
>   for i in range(n-1):
>       min_idx = i
>       for j in range(i+1, n):
>           if a[j] < a[min_idx]:
>               min_idx = j
>       a[i], a[min_idx] = a[min_idx], a[i]
>
>
>
>```   

---

### <b>ⅲ. 셀렉션 알고리즘(Selection Algorithm)</b>
<br>

저장되어 있는 자료로부터 k번째로 큰 혹은 작은 원소를 찾는 방법
- 최소값, 최대값 혹은 중간값을 찾는 알고리즘  

<b>선택 과정</b>
셀렉션은 아래와 같은 과정을 통해 이루어진다.
- 정렬 알고리즘을 이용하여 자료 정렬하기
- 원하는 순서에 있는 원소 가져오기

k번째로 작은 원소를 찾는 알고리즘
- k가 비교적 작을 때 유용, O(kn)의 수행시간 필요
>```python
>def select(arr, k):
>   for i in range(0, k):
>       min_idx = i
>           for j in range(i+1, len(arr)):
>               if arr[j] < arr[min_idx]:
>                   min_idx = j
>           arr[i], arr[min_idx] = arr[min_idx], arr[i]
>   return arr[k-1]
>```





