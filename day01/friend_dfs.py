def dfs_friends(g, start):

    done = set()      # 이미 방문한 사람 집합

    order = []         # 방문 순서 기록

    def _dfs(p):

        done.add(p)      # 방문 기록

        order.append(p)     # 순서 기록

        for x in g[p]:           # 이웃을 하나씩 확인

            if x not in done:  # 미방문이면

                _dfs(x)        # 그 이웃으로 즉시 이동 (재귀 호출)

    _dfs(start)    # 시작 사람에서 탐색 시작

    return order

fr_info = {

    'Summer': ['John', 'Justin', 'Mike'],

    'John':   ['Summer', 'Justin'],

    'Justin': ['John', 'Summer', 'Mike', 'May'],

    'Mike':   ['Summer', 'Justin'],

    'May':    ['Justin', 'Kim'],

    'Kim':    ['May'],

    'Tom':    ['Jerry'],

    'Jerry':  ['Tom'],

}


print("=== DFS: Summer의 모든 친구 ===")

result = dfs_friends(fr_info, 'Summer')

print(result)

print()

print("=== DFS: Jerry의 모든 친구 ===")

result = dfs_friends(fr_info, 'Jerry')

print(result)

def bfs_friends(g, start):

    qu = []

    done = set()

    qu.append(start)

    done.add(start)

    order = []

    while qu:

        p = qu.pop(0)

        order.append(p)

        for x in g[p]:

            if x not in done:

                qu.append(x)

                done.add(x)

    return order


print("=== 비교: Summer에서 시작 ===")

print("BFS:", bfs_friends(fr_info, 'Summer'))

print("DFS:", dfs_friends(fr_info, 'Summer'))
