# Day 01 - 자료구조 & 그래프 탐색 정리
 
---
 
## 수업 목표
- 자료구조 (스택, 큐)
- 그래프 표현
- BFS / DFS
 
---
 
## 용어 정리
 
| 용어 | 설명 |
|---|---|
| **알고리즘** | 문제를 해결하는 순서와 방법 |
| **자료구조** | 데이터를 저장하고 관리하는 방식 |
| **스택 (Stack)** | LIFO - 나중에 넣은 게 먼저 나옴 |
| **큐 (Queue)** | FIFO - 먼저 넣은 게 먼저 나옴 |
| **그래프 (Graph)** | 노드와 간선으로 이루어진 자료구조 |
| **노드 (Node)** | 그래프의 점, 데이터가 저장되는 곳 |
| **간선 (Edge)** | 노드와 노드를 연결하는 선 |
| **BFS** | 너비 우선 탐색 - 가까운 노드부터 탐색 |
| **DFS** | 깊이 우선 탐색 - 한 방향으로 끝까지 탐색 |
| **재귀 (Recursion)** | 함수가 자기 자신을 호출하는 것 |
| **방문 (Visited)** | 이미 간 노드를 체크해서 중복 방문 방지 |
| **LIFO** | Last In First Out - 스택 |
| **FIFO** | First In First Out - 큐 |
 
---
 
## 스택 (Stack)
 
**LIFO - 나중에 넣은 게 먼저 나옴**
 
```python
stack = []
stack.append('A')  # push
stack.append('B')
stack.append('C')
print(stack.pop())  # C 나옴
print(stack.pop())  # B 나옴
```
 
---
 
## 큐 (Queue)
 
**FIFO - 먼저 넣은 게 먼저 나옴**
 
```python
from collections import deque
queue = deque()
queue.append('A')   # enqueue
queue.append('B')
queue.append('C')
print(queue.popleft())  # A 나옴
print(queue.popleft())  # B 나옴
```
 
---
 
## BFS vs DFS 비교
 
| 항목 | BFS | DFS |
|---|---|---|
| 탐색 방식 | 큐 (FIFO) | 스택 / 재귀 (LIFO) |
| 먼저 탐색 | 가까운 곳부터 | 깊은 곳부터 |
| 최단경로 | ✅ 보장 | ❌ 보장 안 함 |
| 활용 | 최단 경로 탐색 | 미로 탐색, 경로 존재 여부 |
 
---
 
## BFS 코드
 
```python
from collections import deque
 
def bfs(graph, start):
    visited = set()
    queue = deque([start])
    visited.add(start)
    order = []
 
    while queue:
        node = queue.popleft()
        order.append(node)
 
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    
    return order
 
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A', 'D'],
    'D': ['B', 'C', 'E'],
    'E': ['D']
}
 
result = bfs(graph, 'A')
print("방문 순서: ", result)
# ['A', 'B', 'C', 'D', 'E']
```
 
---
 
## DFS 코드
 
```python
def dfs_friends(g, start):
    done = set()
    order = []
 
    def _dfs(p):
        done.add(p)
        order.append(p)
        for x in g[p]:
            if x not in done:
                _dfs(x)  # 재귀 호출
 
    _dfs(start)
    return order
```
 
---
 
## 친밀도 (BFS 응용)
 
```python
def print_all_friends(g, start):
    qu = []
    done = set()
    qu.append((start, 0))  # (이름, 친밀도)
    done.add(start)
 
    while qu:
        (p, d) = qu.pop(0)
        print(p, d)
 
        for x in g[p]:
            if x not in done:
                qu.append((x, d + 1))
                done.add(x)
```
 
---
 
## 핵심 포인트
 
- `set()` → 중복 없는 집합, 방문 체크용으로 사용
- `deque` → 리스트보다 `popleft()` 가 빠름
- BFS는 **층별 탐색** → 최단경로 보장
- DFS는 **깊이 탐색** → 재귀 사용
 
---
 
## VSCode 단축키
- 마크다운 미리보기: `Ctrl + Shift + V`