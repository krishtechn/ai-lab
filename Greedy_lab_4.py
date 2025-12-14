import heapq

def greedy_search(graph, heuristic, start, goal):
    pq = [(heuristic[start], start)]
    visited = set()

    while pq:
        h, node = heapq.heappop(pq)

        if node == goal:
            return True

        if node in visited:
            continue

        visited.add(node)
        print(node, end=" ")

        for neighbor in graph[node]:
            if neighbor not in visited:
                heapq.heappush(pq, (heuristic[neighbor], neighbor))

    return False


# Example graph (unweighted)
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

# Heuristic values h(n)
heuristic = {
    'A': 5,
    'B': 4,
    'C': 2,
    'D': 7,
    'E': 1,
    'F': 0
}

greedy_search(graph, heuristic, 'A', 'F')