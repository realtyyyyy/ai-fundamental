# 定义目标状态
goal_state = '12345678x'

# 计算某个状态下空格位置的上下左右可交换的位置
def get_neighbors(state):
    index = state.index('x')
    moves = [(1, 0, 'd'), (-1, 0, 'u'), (0, 1, 'r'), (0, -1, 'l')]
    neighbors = []

    for dx, dy, move in moves:
        x, y = index // 3 + dx, index % 3 + dy
        if 0 <= x < 3 and 0 <= y < 3:
            new_index = x * 3 + y
            neighbor_state = list(state)
            neighbor_state[index], neighbor_state[new_index] = neighbor_state[new_index], neighbor_state[index]
            neighbors.append((''.join(neighbor_state), move))

    return neighbors

# 计算启发函数：曼哈顿距离
def heuristic(state):
    distance = 0
    for i in range(9):
        if state[i] != 'x':
            current_row, current_col = i // 3, i % 3
            target_row, target_col = (int(state[i]) - 1) // 3, (int(state[i]) - 1) % 3
            distance += abs(current_row - target_row) + abs(current_col - target_col)
    return distance

# 使用 A* 算法搜索最短路径
def a_star(start):
    open_set = [(heuristic(start), 0, '', start)]  # 优先队列，用于存储估计值、步数、路径和状态
    closed_set = set()

    while open_set:
        _, steps, path, current_state = min(open_set)
        if current_state == goal_state:
            return path
        open_set.remove((heuristic(current_state) + steps, steps, path, current_state))
        closed_set.add(current_state)

        for neighbor, move in get_neighbors(current_state):
            if neighbor not in closed_set:
                open_set.append((heuristic(neighbor) + steps + 1, steps + 1, path + move, neighbor))

    return "unsolvable"

# 读取输入
initial_state = ''.join(input().split())

# 计算最少移动次数
min_moves = a_star(initial_state)
print(min_moves)