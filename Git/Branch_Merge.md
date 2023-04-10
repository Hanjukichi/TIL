# Git Branch

여러 갈래로 작업 공간을 나누어 독립적으로 작업할 수 있도록 도와주는 Git의 도구

## 장점
- 브랜치는 독립 공간을 형성하기 때문에 원본에 대해 안전함
- 하나의 작업은하나의 브랜치로 나누어 진행되므로 체계적인 개발이 가능
- Git은 브랜치를 만드는 속도가 굉장히 빠르고, 적은 용량을 소모함

## Read, Creat, Delete

### 조회

#### ```git branch```
- 로컬 저장소의 브랜치 목록 확인

#### ```git branch -r```
- 원격 저장소의 브랜치 목록 확인

### 생성

#### ```git branch <branch name>```
- 새로운 브랜치 생성
  
#### ```git branch <branch name>```
- 특정 커밋 기준으로 브랜치 생성

### 삭제

#### ```git branch -d <branch name>```
- 병합된 브랜치만 삭제 가능

#### ```git branch -D <branch name>```
- 강제 삭제

## switch

### ```git switch <branch name>```
- 현재 브랜치에서 다른 브랜치로 이동

### ```git switch -c <branch name>```
- 브랜치를 새로 생성 및 이동

switch 하기 전에, 변경 사항을 반드시 커밋 해야함
- 커밋하지 않은 상태에서 switch를 하면 브랜치를 이동했음에도 해당파일이 그대로 남아있음

## HEAD
- 현재 브랜치의 최신 커밋을 가르킴
- `git log` 혹은 `cat.git/HEAD`를 통해 현재 HEAD가 어떤 브랜치를 가리키는지 알 수 있음

<br>

# Merge

## git merge
```git merge <branch_name>```
- 분기된 브랜치들을 하나로 합치는 명령어
- 주로 master에 병합
- 병합하기 전에 메인 브랜치로 `switch` 해야함
- 세 종류가 존재
  - Fast-Forwad
  - 3-way Merge
  - Merge Conflict

### Fast-Forward
- (메인)브랜치가 가리키는 커밋을 앞으로 이동시키는 방법

### 3-way Merge
- 각 브랜치의 커밋 두 개와 공통 조상 하나를 사용하여 병합하는 방법

### Merge Conflice
- 두 브랜치가 같은 부분을 수정한 경우
  - 어느 브랜치 내용으로 작성해야할지 판단을 못 함
- 보통 같은 파일의 같은 부분을 수정했을 때 자주 발생
- 충돌이 발생한 부분은 작성자가 직접 해결 해야함