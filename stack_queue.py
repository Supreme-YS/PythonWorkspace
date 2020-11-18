#stack and queue

from collections import deque # collections 모듈에서 deque를 가져옴

a = deque([10, 20, 30])

a.append(500) # 덱의 오른쪽에 500 추가

a.popleft() # 덱의 왼쪽 요소 하나 삭제

print(a)
