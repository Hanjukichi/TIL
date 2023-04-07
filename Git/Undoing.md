# Git undoing

## git restore
```git resotre <file_name>```
- 이미 깃에 추가가된 파일의 타겟
- git이 추적하고 있던 마지막 상태로 되돌리기

## git rm --cached
```git rm --cached <file_name>```
- 아직 git에 추가되지 않은 파일이 add 되었을 때 되돌리기

## git restore --staged
```git restore --staged <file_name>```
- git에 추가되었던 파일의 수정사항이 add 되었을 때 되돌리기

## git commit --amend
```git commit --amend```
- 직전 이력의 메시지를 수정하기

## git commit --amend(with new changeds)
```git commit --amend```
- commit 메시지를 수정하고 add된 파일들을 직전 commit에 추가