'''
정수(1 ~ 100) 1개가 입력되었을 때 카운트다운을 출력해보자.

while 조건식 :
  ...
  ...

반복 실행구조를 사용해 보자.

참고
조건검사, 출력, 감소의 순서와 타이밍을 잘 생각해보자.

'''

n = int(input())
n = n-1
while n != -1:
    print(n)
    n = n-1