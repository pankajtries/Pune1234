from collections import defaultdict, deque

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def dfs(self, start_vertex, visited=None):
        if visited is None:
            visited = set()
        visited.add(start_vertex)
        print(start_vertex, end=" ")
        for neighbor in self.graph[start_vertex]:
            if neighbor not in visited:
                self.dfs(neighbor, visited)

    def bfs(self, start_vertex):
        visited = set()
        queue = deque([start_vertex])
        visited.add(start_vertex)
        while queue:
            vertex = queue.popleft()
            print(vertex, end=" ")
            for neighbor in self.graph[vertex]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

g = Graph()

m = int(input("Enter no of edges: "))
for _ in range(m):
    u, v = map(int, input("Enter the edge (u v): ").split())
    g.add_edge(u, v)

while True:
    print("1. Depth First Search (DFS)")
    print("2. Breadth First Search (BFS)")
    print("3. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        start_vertex = int(input("Enter the starting vertex for DFS: "))
        print("DFS:")
        g.dfs(start_vertex)
        print()
    elif choice == 2:
        start_vertex = int(input("Enter the starting vertex for BFS: "))
        print("BFS:")
        g.bfs(start_vertex)
        print()
    elif choice == 3:
        break
    else:
        print("Invalid choice. Please try again.")
