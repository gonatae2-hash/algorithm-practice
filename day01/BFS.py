'''
    큐에 시작 노드 넣기
    방문 표시

    큐가 비어있지 않는 동안:
        현재 = 큐에서 꺼내기
        현재 노드 처리

        현재의 이웃들에 대해:
            방문하지 않았으면:
                방문 표시
                큐에 넣기
'''
from collections import deque

def bfs(graph, start):
    visited = set()
    queue = deque({start})
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
    'A' : ['B', 'C'],
    'B' : ['A', 'D'],
    'C' : ['A', 'D'],
    'D' : ['B', 'C', 'E'],
    'E' : ['D']
    }

result =bfs(graph,'A')
print("방문 순서: ", result)