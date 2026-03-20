import heapq

# VisuAlgo에서 입력한 것과 동일한 그래프

# {노드: [(이웃, 비용), ...]} 형태

graph = {

    0: [(1, 1), (2, 4)],

    1: [(2, 2), (3, 5)],

    2: [(3, 1), (4, 3)],

    3: [(4, 2)],

    4: []

}


def dijkstra(graph, start):

    distances = {node: float('inf') for node in graph}

    distances[start] = 0

    heap = []

    heapq.heappush(heap, (0, start))

    visited = set()

    while heap:

        cost, node = heapq.heappop(heap)

        if node in visited:

            continue

        visited.add(node)

        print(f"  확정: 노드 {node}, 비용 {cost}")  # 디버그 출력

        for neighbor, weight in graph[node]:

            new_cost = cost + weight

            if new_cost < distances[neighbor]:

                distances[neighbor] = new_cost

                heapq.heappush(heap, (new_cost, neighbor))

                print(f"    → 노드 {neighbor} 업데이트: {new_cost}")  # 디버그 출력

    return distances


print("=== Dijkstra 실행 과정 ===")

result = dijkstra(graph, 0)

print()

print("=== 최종 결과 ===")

print(result)

import heapq

def dijkstra_practice(graph, start):

    # 1. 모든 노드의 거리를 무한대로 초기화

    distances = {node: float('inf') for node in graph}

    distances[start] = 0    # 시작 노드는 0

    # 2. 우선순위 큐 (Day 1의 deque 대신)

    heap = []

    heapq.heappush(heap, (0, start))   # (비용, 노드) 형태로 넣기

    # 3. 방문 확인 집합 (Day 1의 done과 같은 역할)

    visited = set()

    while heap:

        # 4. 비용이 가장 작은 노드 꺼내기 (Day 1: queue.popleft())

        cost, node = heapq.heappop(heap)

        if node in visited:    # 이미 확정된 노드면 건너뜀

            continue

        visited.add(node)

        # 5. 이웃 탐색 (Day 1: for x in g[p])

        for neighbor, weight in graph[node]:

            new_cost = cost + weight    # 현재 비용 + 간선 비용

            if new_cost < distances[neighbor]:    # 더 짧은 경로 발견 시

                distances[neighbor] = new_cost    # 거리 업데이트

                heapq.heappush(heap, (new_cost, neighbor))  # 큐에 추가

    return distances


# 테스트

graph2 = {

    0: [(1, 2), (2, 5)],

    1: [(2, 1), (3, 7)],

    2: [(3, 3)],

    3: []

}

print("=== 빈칸 채우기 테스트 ===")

result2 = dijkstra_practice(graph2, 0)

print(result2)
