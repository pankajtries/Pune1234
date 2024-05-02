class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []

    def add_edge(self, u, v, w):
        self.graph.append((u, v, w))

    def find(self, parent, i):
        if 0 <= i < len(parent):
            return i if parent[i] == i else self.find(parent, parent[i])
        else:
            return i

    def union(self, parent, rank, x, y):
        xroot = self.find(parent, x)
        yroot = self.find(parent, y)
        if 0 <= xroot < len(rank) and 0 <= yroot < len(rank):
            if rank[xroot] < rank[yroot]:
                parent[xroot] = yroot
            elif rank[xroot] > rank[yroot]:
                parent[yroot] = xroot
            else:
                parent[yroot] = xroot
                rank[xroot] += 1

    def kruskal_algo(self):
        result = []
        self.graph.sort(key=lambda x: x[2])
        parent = list(range(self.V))
        rank = [0] * self.V  # Initialize rank list with the correct size
        for u, v, weight in self.graph:
            x = self.find(parent, u)
            y = self.find(parent, v)
            if x != y:
                result.append((u, v, weight))
                self.union(parent, rank, x, y)
        for u, v, weight in result:
            print(f"{u} - {v}: {weight}")


def get_user_input():
    vertices = int(input("Enter the number of vertices: "))
    g = Graph(vertices)
    edges = int(input("Enter the number of edges: "))
    for _ in range(edges):
        u, v, weight = map(int, input("Enter edge (u v weight): ").split())
        g.add_edge(u, v, weight)
    return g


def main():
    g = get_user_input()
    print("Minimum Spanning Tree:")
    g.kruskal_algo()


if __name__ == "__main__":
    main()
