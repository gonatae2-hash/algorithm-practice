def dfs(graph, start):
    visited = set()
    order = []

    def _dfs(node): # 내부 함수 - 자기 자신을 다시 호출(재귀)
        visited.add(node)
        order.append(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                _dfs(neighbor) # 더 깊이 이동

    _dfs(start)
    return order

graph = {
    'A' : {'B', 'C'},
    'B' : {'A', 'D'},
    'C' : {'A', 'D'},
    'D' : {'B', 'C', 'E'},
    'E' : {'D'}
}
