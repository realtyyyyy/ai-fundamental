import heapq

def dijkstra(graph, start, end):
    pq = [(0, start)]
    visited = set()

    while pq:
        cost, node = heapq.heappop(pq)
        if node == end:
            return cost
        if node in visited:
            continue
        visited.add(node)
        for neighbor, weight in graph[node]:
            if neighbor not in visited:
                heapq.heappush(pq, (cost + weight, neighbor))

    return -1

def shortest_path(n, m, edges):
    graph = {i: [] for i in range(1, n+1)}
    for x, y, z in edges:
        graph[x].append((y, z))

    return dijkstra(graph, 1, n)

# 读取输入
n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]

# 计算最短距离并输出结果
result = shortest_path(n, m, edges)
print(result)