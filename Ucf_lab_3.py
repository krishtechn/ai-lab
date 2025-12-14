import heapq

def uniform_cost_search(graph, start, goal):
    pq = [(0, start)]  # (cost, node)
    visited = {}

    while pq:
        cost, node = heapq.heappop(pq)

        if node == goal:
            return cost

        if node in visited and visited[node] <= cost:
            continue

        visited[node] = cost

        for neighbor, weight in graph[node]:
            heapq.heappush(pq, (cost + weight, neighbor))

    return float("inf")

# Example weighted graph (adjacency list)
graph = {
    'A': [('B', 2), ('C', 4)],
    'B': [('D', 7), ('E', 1)],
    'C': [('F', 3)],
    'D': [],
    'E': [('F', 1)],
    'F': []
}

result = uniform_cost_search(graph, 'A', 'F')
print("Minimum Cost from A to F:", result)


# output:
# Minimum Cost from A to F: 4
# (A → B → E → F = 2 + 1 + 1 = 4)


