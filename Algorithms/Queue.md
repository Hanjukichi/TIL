# <b>큐</b>
<br><br>

## <b>Ⅰ. 큐(Queue)란?</b>

---

### <b>ⅰ. 큐의 특성</b>
<br>

삽입과 삭제의 위치가 제한적인 자료 구조
- 삽입: 큐의 뒤
- 삭제: 큐의 앞

선입선출구조(FIFP: First In First Out)
- 큐에 삽입한 순서대로 원소가 저장됨
- 가장 먼저 삽입된 원소는 가장 먼저 삭제

---

### <b>ⅱ. 큐의 기본 구조</b>
<br>

큐의 선입선출 구조
|머리||||||||꼬리|
|---|---|---|---|---|---|---|---|---|
|삭제|a|b|c|d|e|f|g|삽입|
|←||||||||←|
- 머리(Front): 첫번째 원소
- 꼬리(Rear): 마지막 원소

큐의 기본 연산
- 삽입: enQueue
- 삭제: deQueue

---

### <b>ⅲ. 큐의 주요 연산</b>
<br>

연산|기능
---|---
enQueue()|뒤쪽에 원소를 삽입
deQueue()|앞쪽 원소를 삭제하고 반환
createQueue()|공백 상태의 큐를 생성
isEmpty()|큐가 공백상태인지 확인
isFull()|큐가 포화상태인지 확인
Qpeek()|앞쪽 원소를 삭제없이 반환


---

### <b>ⅳ. 큐의 연산 과정</b>
<br>

(1) 공백 큐 생성 : createQueue()
|머리|0|1|2|3|4|5|6|꼬리|
|---|---|---|---|---|---|---|---|---|
|삭제||||||||삽입|

(2) A 삽입 : enQueue(A)
|머리|0|1|2|3|4|5|6|꼬리|
|---|---|---|---|---|---|---|---|---|
|삭제|A|||||||삽입|

(3) B 삽입 : enQueue(B)
|머리|0|1|2|3|4|5|6|꼬리|
|---|---|---|---|---|---|---|---|---|
|삭제|A|B||||||삽입|

(4) 원소 반환/삭제 : deQueue()
||머리|1|2|3|4|5|6|꼬리|
|---|---|---|---|---|---|---|---|---|
||A|B||||||삽입|

(5) C 삽입 : enQueue(C)
||머리|1|2|3|4|5|6|꼬리|
|---|---|---|---|---|---|---|---|---|
|삭제|A|B|C|||||삽입|

(6) 원소 반환/삭제 : deQueue()
||0|머리|2|3|4|5|6|꼬리|
|---|---|---|---|---|---|---|---|---|
|삭제|A|B|C|||||삽입|

(7) 원소 반환/삭제 : deQueue()
||0|1|머리|3|4|5|6|꼬리|
|---|---|---|---|---|---|---|---|---|
|삭제|A|B|C|||||삽입|

<br><br>


## <b>Ⅱ. 선형큐</b>

---

### <b>ⅰ. 선형 큐란?</b>
<br>

1차원 배열을 이용한 큐
- 큐의 크기 = 배열의 크기
- front: 저장된 첫 번째 원소의 인덱스
- rear: 저장된 마지막 원소의 인덱스  

상태표현
- 초기 상태: front = rear = -1
- 공백 상태: front == rear
- 포화 상태: rear == n-1  
(n : 배열의 크기)

---

### <b>ⅱ. 선형 큐의 구현</b>  
<br>

1. 초기 공백 큐 생성  
    - 크기 n인 1차원 배열 생성
    - front와 rear를 -1로 초기화  
<br>
2. 삽입: enQueue(item)  
마지막 원소 뒤에 새로운 원소를 삽입하기 위해
    - rear 값을 하나 증가 > 삽입할 자리 마련
    - Q[rear]에 원소 저장
>```python
>def enQueue(item):
>   global rear
>   if isFull(): 
>       print("Queue_Full")
>   else:
>       rear += 1
>       Q[rear] = item  

3. 삭제/반환: deQueue()  
가장 앞 원소를 삭제하기 위해
    - front값을 하나 증가 > 첫번째 원소 이동
    - 새로운 첫 번째 원소를 리턴
>```python
>def deQueue():
>   global front
>   if isEmpty(): 
>       print("Queue_Empty")
>   else:
>       front += 1
>       return Q[front]

4. 공백상태 및 포화상태 검사
    - 공백상태[isEmpty()]: Front == rear
    - 포화상태[isFull()]: rear == n-1
>```python
>def isEmpty():
>   return front == rear
>
>def isFull():
>   return rear == len(Q)-1

5. 검색 : Qpeek()
    - 가장 앞에 있는 원소를 검색하여 반환하는 연산
    - 큐 첫 번째에 있는 원소를 반환
>```python
>def Qpeek():
>   global front
>   if isEmpty(): 
>       print("Queue_Empty")
>   else:
>       return Q[front+1]

---

### <b>ⅲ. 선형 큐의 문제점</b>  
<br>

잘못된 포화상태 인식
- 배열의 앞부분에 활용 공간이 남아있음
- rear = n-1인 상태가 되면 포화상태로 인식
- 더 이상 삽입 수행 x  

해결 방법 1
- 매 연산마다 저장된 원소들을 배열 앞부분으로 모두 이동
- 원소 이동에 많은 시간이 소요됨
- 큐의 효율성이 급격히 떨어짐  

해결 방법 2
- 1차원 배열을 사용함
- 논리적으론 배열의 처음과 끝이 연결
- 원형 형태의 큐를 이룬다고 가정  

원형 큐의 논리적 구조
|6과 연결|0|1|2|3|4|5|6|0과 연결|
|---|---|---|---|---|---|---|---|---|
|삭제|A|B|C|||||삽입|  

<br><br>


## <b>Ⅲ. 원형큐</b>

---

### <b>ⅰ. 원형 큐의 구조</b>
<br>

초기 공백 상태
- front = 0
- rear = 0

Index의 순환
1. front와 rear가 n-1을 가리킴
2. 논리적 순환을 통해 0으로 이동해야함
3. 이를 위해 나머지 연산자 mod를 사용

front 변수
- 공백 상태와 포화상태 구분을 쉽게 할 필요있음
- front가 있는 자리는 사용하지 않고 빈자리로 둠

삽입 위치 및 삭제 위치
||삽입 위치|삭제 위치|
|---|---|---|
|선형큐|rear += 1|front += 1|
|원형큐|rear = (rear + 1) % n|front = (front + 1) % n|

### <b>ⅱ. 원형 큐의 구현</b>  
<br>

1. 초기 공백 큐 생성  
    - 크기 n인 1차원 배열 생성
    - front와 rear를 0으로 초기화  
<br>


2. 공백상태 및 포화상태 검사
    - 공백상태: isEmpty()
    - 포화상태: isFull()
>```python
>def isEmpty():
>   return front == rear
>
>def isFull():
>   return (rear + 1)%n == front

3. 삽입: enQueue(item)  
마지막 원소 뒤에 새로운 원소를 삽입하기 위해
    - rear 값을 조정 > 삽입할 자리 마련
    - rear = (rear + 1) % n
    - Q[rear]에 원소 저장

>```python
>def enQueue(item):
>   global rear
>   if isFull(): 
>       print("Queue_Full")
>   else:
>       rear = (rear + 1) % n
>       Q[rear] = item  

4. 삭제/반환: deQueue(), delete()  
가장 앞 원소를 삭제하기 위해
    - front값을 하나 증가 > 첫번째 원소 이동
    - 새로운 front 원소를 리턴
>```python
>def deQueue():
>   global front
>   if isEmpty(): 
>       print("Queue_Empty")
>   else:
>       front = (front + 1) % n
>       return Q[front]

<br><br>


## <b>Ⅳ. 우선순위 큐(Priority Queue)</b>

---

### <b>ⅰ. 원형 큐의 기본 특징</b>
<br>

특성
- 우선순위를 가진 항목들을 저장하는 큐
- FIFO 순서가 아니라 우선순위가 높은 순서대로 먼저 나감  

적용 분야
- 시뮬레이션 시스템
- 네트워크 트래픽 제어
- 운영체제의 테스크 스케줄링

---

### <b>ⅱ. 배열을 이용한 우선순위 큐</b>
<br>

배열을 이용한 우선순위 큐 구현
- 배열을 이용하여 자료 저장
- 원소를 삽입하면서 우선순위를 비교하여 적절한 위치에 삽입
- 가장 앞에 최고 우선순위의 원소 위치

문제점
- 배열을 사용 > 삽입이나 삭제 연산 때 원소의 재배치 발생
- 이에 소요되는 시간이나 메모리 낭비 큼

<br><br>


## <b>Ⅴ. 버퍼</b>

---

### <b>ⅰ. 버퍼란?</b>
<br>

데이터를 전송하는 동안 일시적으로 그 데이터를 보관하는 메모리의 영역  

버퍼링
- 버퍼를 활용하는 방식 또는 버퍼를 채우는 동작을 의미

버퍼의 자료 구조
- 일반적으로 입출력 및 네트워크 와 관련된 기능에 이용
- 순서대로 입/출력/전달되어야함
- FIFO 방식의 자료구조인 큐가 활용됨

키보드 버퍼(예시)
- 사용자 입력 : A P S enter
- 키보드 입력 버퍼 : A P S enter
- 입력 버퍼에 enter 들어옴 : enter S P A → 연산

<br><br>


## <b>Ⅴ. 넓이 우선 탐색(Breadth First Searh)</b>

---

### <b>ⅰ. BFS란?</b>
<br>

그래프를 탐색하는 방법 중 하나  

탐색 시작점의 인접한 정점들을 먼저 모두 차례로 방문 후, 방문했던 정점을 시작점으로 하여 다시 인접한 정점들을 차례로 방문하는 방식  


인접한 정점들에 대해 탐색을 한 후, 차례로 다시 너비우선탐색을 진행해야 하므로, 선입선출 형태의 자료구조인 큐를 활용함

---

### <b>ⅰ. BFS 알고리즘</b>
<br>

visited: 방문했음을 나타냄
>```python
># G: 그래프, v: 탐색 시작점
>def BFS(G ,v, n):
>   visited = [0] * (n+1)
>   queue = []
>   queue.append(v)
>   while queue:
>       t = queue.pop(0)    
>       if not visited[t]:
>           visited[t] = True
>           visit[t]  # 정점 t에서 할 일
>           for i in G[t]:
>               if not visited[i]:
>                   queue.append(i)
>```

visited: 인큐임을 나타냄
>```python
># G: 그래프, v: 탐색 시작점
>def BFS(G ,v, n):
>   visited = [0] * (n+1)
>   queue = []
>   queue.append(v)
>   visited[v] = 1
>   while queue:
>       t = queue.pop(0)
>       visit[t]  # 정점 t에서 할 일  
>       for i in G[t]: 
>           if not visited[t]               
>               queue.append(i)
>               visited[i] = 1
>```

visited: 출발지로부터의 거리
>```python
># G: 그래프, v: 탐색 시작점
>def BFS(G ,v, n):
>   visited = [0] * (n+1)
>   queue = []
>   queue.append(v)
>   visited[v] = 1
>   while queue:
>       t = queue.pop(0)
>       visit[t]  # 정점 t에서 할 일  
>       for i in G[t]: 
>           if not visited[t]               
>               queue.append(i)
>               visited[i] = 1
>```

