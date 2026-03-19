from collections import deque

def bfs_grid(grid, start, goal):
    rows, cols = len(grid), len(grid[0]) # 격자 크기 : 5행 5열
    queue = deque([(start, [start])]) # (좌표, [경로]) 형태로 저장
    visited = {start} # 이미 탐색한 좌표 집합 (done이랑 같은 역할)

    # 상, 하, 좌, 우 이동
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while queue:
        (r, c), path = queue.popleft() # 큐에서 (현재 좌표, 여기까지 온 경로(path))

        if (r, c) == goal: # 목표에 도달하면
            return path # 경로 반환하고 끝

        for dr, dc in directions:   # 상하좌우 4방향 확인
            nr, nc = r + dr, c + dc # 새 좌표 계산 
            if (0 <= nr < rows and 0 <= nc < cols # 격자 범위 안에 있고
                    and (nr, nc) not in visited   # 아직 방문 안에 있고
                    and grid[nr][nc] != '#'):     # (#) 벽이 아니면
                visited.add((nr, nc))             # 방문을 기록한다
                queue.append(((nr, nc), path + [(nr, nc)])) # 경로에 추가하여 큐에 넣기

    return None  # 경로 없음


# 격자 맵 정의
grid = [
    ['S', '.', '.', '#', '.'],
    ['.', '#', '.', '#', '.'],
    ['.', '#', '.', '.', '.'],
    ['.', '.', '#', '#', '.'],
    ['.', '.', '.', '.', 'G'],
]

path = bfs_grid(grid, (0, 0), (4, 4))
print("최단 경로:", path)
print("이동 횟수:", len(path) - 1)