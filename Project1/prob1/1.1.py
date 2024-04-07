from collections import deque

def shortest_path(n, m, edges):
    graph = {i: [] for i in range(1, n+1)}
    for a, b in edges:
        graph[a].append(b)

    visited = set()
    queue = deque([(1, 0)])  # (node, distance)

    while queue:
        node, distance = queue.popleft()
        if node == n:
            return distance
        if node in visited:
            continue
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                queue.append((neighbor, distance + 1))

    return -1

# 读取输入
n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]

# 计算最短距离并输出结果
result = shortest_path(n, m, edges)
print(result)