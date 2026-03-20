# Day 02 - 가중치 그래프 & 최단경로 알고리즘 정리
 
---
 
## 용어 정리
 
| 용어 | 설명 |
|---|---|
| **가중치 (Weight)** | 간선(이동)에 붙는 비용 - 거리, 시간, 위험도 등 |
| **우선순위 큐** | 값이 작은 게 먼저 나오는 큐 |
| **heapq** | Python 우선순위 큐 라이브러리 |
| **Dijkstra** | 가중치 있는 그래프에서 최소 비용 경로 탐색 |
| **휴리스틱** | 목적지까지 예상 거리 (정확하진 않지만 빠른 추정) |
| **A*** | Dijkstra + 휴리스틱 결합 (더 빠른 최단경로) |
| **g** | 시작점으로부터 현재까지 실제 비용 |
| **h** | 현재에서 목적지까지 예상 비용 (휴리스틱) |
| **f** | g + h (총 예상 비용) |
| **global_planner** | ROS에서 A*/Dijkstra로 전체 경로 계획하는 모듈 |
 
---
 
## BFS vs Dijkstra 차이
 
| 항목 | BFS | Dijkstra |
|---|---|---|
| 가중치 | ❌ 없음 | ✅ 있음 |
| 탐색 기준 | 최소 이동 횟수 | 최소 비용 경로 |
| 자료구조 | 큐 | 우선순위 큐 |
 
---
 
## heapq 사용법
 
```python
import heapq
 
heap = []
heapq.heappush(heap, 5)
heapq.heappush(heap, 1)
heapq.heappush(heap, 3)
 
print(heapq.heappop(heap))  # 1 (가장 작은 값)
print(heapq.heappop(heap))  # 3
print(heapq.heappop(heap))  # 5
```
 
---
 
## Dijkstra 코드
 
```python
import heapq
 
def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
 
    heap = []
    heapq.heappush(heap, (0, start))  # (비용, 노드)
 
    visited = set()
 
    while heap:
        cost, node = heapq.heappop(heap)
 
        if node in visited:
            continue
        visited.add(node)
 
        for neighbor, weight in graph[node]:
            new_cost = cost + weight
 
            if new_cost < distances[neighbor]:
                distances[neighbor] = new_cost
                heapq.heappush(heap, (new_cost, neighbor))
 
    return distances
 
graph = {
    0: [(1, 1), (2, 4)],
    1: [(2, 2), (3, 5)],
    2: [(3, 1), (4, 3)],
    3: [(4, 2)],
    4: []
}
 
result = dijkstra(graph, 0)
print(result)
# {0: 0, 1: 1, 2: 3, 3: 4, 4: 6}
```
 
---
 
## Dijkstra 동작 흐름
 
```
시작: 0
초기: {0:0, 1:∞, 2:∞, 3:∞, 4:∞}
 
0 처리 → 1=1, 2=4 업데이트
1 처리 → 2=3(1+2), 3=6 업데이트
2 처리 → 3=4(3+1), 4=6 업데이트
3 처리 → 4=6(4+2) 업데이트
4 처리 → 종료
 
최종: {0:0, 1:1, 2:3, 3:4, 4:6}
```
 
---
 
## A* 알고리즘
 
**f = g + h**
 
| 변수 | 의미 |
|---|---|
| `g` | 시작점에서 현재까지 실제 비용 (상하좌우 = 10, 대각선 = 14) |
| `h` | 현재에서 목적지까지 예상 거리 (휴리스틱) |
| `f` | g + h (총 예상 비용, 낮을수록 먼저 탐색) |
 
---
 
## Dijkstra vs A* 비교
 
| 항목 | Dijkstra | A* |
|---|---|---|
| 휴리스틱 | ❌ 없음 | ✅ 있음 |
| 탐색 방향 | 모든 방향 | 목적지 방향 위주 |
| 속도 | 느림 | 빠름 |
| 최단경로 | ✅ 보장 | ✅ 보장 |
 
---
 
## ROS global_planner
 
```
[현재위치]
    ↓
global_planner (A* / Dijkstra)
    ↓
[전체 경로 계획]
    ↓
[로봇 이동]
```
 
- costmap의 비용이 높은 칸 = 장애물 근처
- Dijkstra/A*가 비용 낮은 경로 선택 → 자연스럽게 장애물 회피
 
---
 
## inflation_radius와 grid 비교
 
```
inflation_radius 작을 때:     inflation_radius 클 때:
1  1  1  1  1                1  1  9  9  1
1  1  1  9  1                1  9  9  9  9
1  1  ■  9  1                1  9  ■  9  9
1  1  1  9  1                1  9  9  9  9
1  1  1  1  1                1  1  9  9  1
```
 
inflation 클수록 장애물 멀리 돌아서 이동!
 
---
 
## 핵심 포인트
 
- `float('inf')` → 무한대 초기화
- heapq는 **(비용, 노드)** 튜플로 넣기
- 비용 같으면 **먼저 들어간 순서**대로 처리
- directions 순서가 경로에 영향을 줌