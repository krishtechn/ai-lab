import heapq

def a_star(graph, heuristic, start, goal):
    pq = [(heuristic[start], 0, start)]  # (f, g, node)
    visited = {}

    while pq:
        f, g, node = heapq.heappop(pq)

        if node == goal:
            return f, g   # return total f and actual path cost g

        if node in visited and visited[node] <= g:
            continue

        visited[node] = g
        print(node, end=" ")

        for neighbor, cost in graph[node]:
            new_g = g + cost
            new_f = new_g + heuristic[neighbor]
            heapq.heappush(pq, (new_f, new_g, neighbor))

    return float("inf"), float("inf")


# Weighted graph
graph = {
    'A': [('B', 2), ('C', 3)],
    'B': [('D', 4), ('E', 2)],
    'C': [('F', 4)],
    'D': [],
    'E': [('F', 1)],
    'F': []
}

# Heuristic values h(n)
heuristic = {
    'A': 6,
    'B': 4,
    'C': 4,
    'D': 7,
    'E': 1,
    'F': 0
}

result = a_star(graph, heuristic, 'A', 'F')
print("\nFinal Cost (g):", result[1])
