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

