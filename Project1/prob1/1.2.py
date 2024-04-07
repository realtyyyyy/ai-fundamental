def dijkstra(graph, start, end):
    n = len(graph)
    # 初始化距离数组
    distance = [float('inf')] * n
    distance[start] = 0

    # 标记已访问的节点
    visited = [False] * n

    for _ in range(n):
        # 找到距离起点最近且未访问的节点
        min_distance = float('inf')
        min_index = -1
        for i in range(n):
            if not visited[i] and distance[i] < min_distance:
                min_distance = distance[i]
                min_index = i

        if min_index == -1:
            break

        visited[min_index] = True

        # 更新最短距离
        for j in range(n):
            if graph[min_index][j] > 0 and not visited[j]:
                distance[j] = min(distance[j], distance[min_index] + graph[min_index][j])

    return distance[end] if distance[end] != float('inf') else -1

def shortest_path(n, m, edges):
    # 构建邻接矩阵
    graph = [[0] * n for _ in range(n)]
    for x, y, z in edges:
        graph[x - 1][y - 1] = z

    return dijkstra(graph, 0, n - 1)

# 读取输入
n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]

# 计算最短距离并输出结果
result = shortest_path(n, m, edges)
print(result)