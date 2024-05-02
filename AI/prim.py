def prims_algorithm():
    n = int(input("Enter Number of Nodes: "))
    mat = [[0]*n for _ in range(n)]
    m = int(input("Enter Number of Edges: "))
    for i in range(m):
        print("Enter Details of Edge "+str(i+1)+" as start end weight")
        start, end, weight = map(int, input().split())
        mat[start][end] = weight
        mat[end][start] = weight
    print("Adjacency Matrix:")
    for row in mat:
        print(" ".join(map(str, row)))

    # Prim's algorithm
    visited = [0]*n
    visited[0] = 1
    tree = []
    while len(tree) < n-1:
        min = float('inf')
        x = 0
        y = 0
        for i in range(n):
            if visited[i]:
                for j in range(n):
                    if ((not visited[j]) and mat[i][j]):
                        if min > mat[i][j]:
                            min = mat[i][j]
                            x = i
                            y = j
        tree.append((x, y, min))
        visited[y] = 1
    for edge in tree:
        print(edge)

# Test the Prim's algorithm function
prims_algorithm()
"""
Enter Number of Nodes: 3
Enter Number of Edges: 3
Enter Details of Edge 1 as start end weight
0 1 4
Enter Details of Edge 2 as start end weight
0 2 3
Enter Details of Edge 3 as start end weight
1 2 2
"""
