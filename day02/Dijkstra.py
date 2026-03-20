import heapq

def dijkstra(graph, start):
    # graph: {노드: [(이웃,비용), ...]} 형태
    # 예: {'A': [('B', 1), ('C', 4)], 'B': [('C', 2), ('D', 5)], ...}

    distances = {node: float('inf') for node in graph} # 모든 노드의 거리를 무한대로 초기화
    distances[start] = 0 # 시작 노드는 0

    heap = [] # 우선순위 큐
    heapq.heappush(heap, (0, start)) # (비용, 노드) 형태로 넣기

    visited = set() # 이미 확정된 노드

    while heap:
        cost, node = heapq.heappop(heap)

        if node in visited : # 이미 확정된 노드면 건너뜀
            continue
        visited.add(node)

        for neighbor, weight in graph[node]:
            new_cost = cost + weight

            if new_cost < distances[neighbor]:
                distances[neighbor] = new_cost # 거리 업데이트
                heapq.heappush(heap, (new_cost, neighbor)) # 큐에 추가

        return distances # 시작 노드에서 모든 노드까지의 최단 거리
    
# 수업에서 바로 실행할 수 있는 예시 그래프 (visualgo 노드 번호와 동일)
graph = {
    0: [(1, 1), (2, 4)],
    1: [(2, 2), (3, 5)],
    2: [(3, 1), (4, 3)],
    3: [(4, 2)],
    4: []
}

# 실행
result = dijkstra(graph, 0)
print(result)
# 출력: {0: 0, 1: 1, 2: 3, 3: 4, 4: 6}
#        0→0: 0
#        0→1: 1           (0 -1→ 1)
#        0→2: 3           (0 -1→ 1 -2→ 2)  ← 직접 가면 4인데, 1을 거치면 3
#        0→3: 4           (0 -1→ 1 -2→ 2 -1→ 3)
#        0→4: 6           (0 -1→ 1 -2→ 2 -3→ 4)