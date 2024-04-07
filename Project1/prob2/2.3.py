import heapq

# 定义目标状态
goal_state = '12345678x'

# 计算某个状态下空格位置的上下左右可交换的位置
def get_neighbors(state):
    index = state.index('x')
    moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    neighbors = []

    for dx, dy in moves:
        x, y = index // 3 + dx, index % 3 + dy
        if 0 <= x < 3 and 0 <= y < 3:
            new_index = x * 3 + y
            neighbor_state = list(state)
            neighbor_state[index], neighbor_state[new_index] = neighbor_state[new_index], neighbor_state[index]
            neighbors.append((''.join(neighbor_state), 1))  # 交换一次

    return neighbors

# 使用 Dijkstra 算法搜索最短路径
def dijkstra(start):
    heap = [(0, start)]  # 优先队列，用于存储状态和到达该状态的最小步数
    visited = set()

    while heap:
        steps, current_state = heapq.heappop(heap)
        if current_state == goal_state:
            return steps
        if current_state in visited:
            continue
        visited.add(current_state)

        for neighbor, cost in get_neighbors(current_state):
            heapq.heappush(heap, (steps + cost, neighbor))

    return -1  # 无解情况

# 读取输入
initial_state = input().replace(' ', '')

# 计算最少交换次数
min_swaps = dijkstra(initial_state)
print(min_swaps)