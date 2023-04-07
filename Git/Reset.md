# Git Reset

## git reset
```git reset <option> <commit id>```
- 프로젝트를 특정 커밋 상태로 되돌림
- 해당 커밋 이후로 쌓았던 커밋들은 전부 사라짐
- 옵션은 soft, mixed, hard 중 하나를 작성
- ID는 되돌아가고 싶은 시점의 커밋 ID를 작성

### --soft
- 되돌아간 커밋 이후 파일들을 Staging Area로 돌려놓음

### --mixed
- 되돌아간 커밋 이후 파일들을 Woring Directory로 돌려놓음
- git reset 옵션 기본값

### --hard
- 되돌아간 커밋 이후의 파일들은 모두 완전 삭제
- 사용시 주의
- 기존 commit 한 적 없는 파일은 그대로 남아있음

### HEAD~<number>
- 입력한 숫자만큼의 전 커밋 내용으로 돌아감
- commit id 대신 입력

## git reflog
```git reflog```
- reset 하기 전의 과거 커밋 내역을 모두 조회 가능
- 이후 해당 거밋으로 reset 하면 hard 옵션으로 삭제된 파일도 복구 가능

## git revert
```git revert <commit id>```
- 이전 커밋을 취소한다는 새로운 커밋을 생성
- Github를 이용할 협업할 때, 커밋 내역의 차이로 인한 충돌 방지 가능