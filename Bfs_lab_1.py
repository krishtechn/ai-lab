from collections import deque
def bfs(graph,start):
    visited = set()
    queue = deque([start])
    while queue:
        node = queue.popleft()
        if node not in visited:
            print(node,end="");
            visited.add(node)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    queue.append(neighbor)

graph = {
    1:[2,3],
    2:[4,5],
    3:[4],
    4:[5],
    5:[]
}

bfs(graph,1);