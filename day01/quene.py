# enquene : 뒤에 데이터 추가 
# dequene : 앞의 데이터를 꺼냄 

from collections import deque

queue = deque()
queue.append('A') # enqueue A -> deque(['A'])  
queue.append('B') # enqueue B -> deque(['A','B'])
queue.append('C') # enqueue C -> deque (['A','B','C'])
print(queue.popleft()) # -> 'A' (가장 먼저 넣은 A가 먼저나옴)
print(queue.popleft()) # -> 'B'