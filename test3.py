from collections import deque

class Node:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def bfs_traversal(grid, start, destination):
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    n = len(grid)
    visited = [[False] * n for _ in range(n)]
    parent = {}

    queue = deque([start])
    visited[start.x][start.y] = True

    while queue:
        current = queue.popleft()

        if current.x == destination.x and current.y == destination.y:
            return construct_path(parent, destination)

        for dx, dy in directions:
            new_x, new_y = current.x + dx, current.y + dy

            if 0 <= new_x < n and 0 <= new_y < n and grid[new_x][new_y] == 0 and not visited[new_x][new_y]:
                visited[new_x][new_y] = True
                parent[(new_x, new_y)] = current
                queue.append(Node(new_x, new_y))

    return None  # No path found

def construct_path(parent, destination):
    path = []
    current = destination
    while current in parent:
        path.append(current)
        current = parent[current]
    path.append(current)  # Add the start node
    path.reverse()
    return path

def main():
    N = int(input("Enter the size of the grid (N x N): "))
    grid = []
    for i in range(N):
        row = list(map(int, input(f"Enter row {i+1} of the grid (0 for empty, 1 for obstacle): ").split()))
        grid.append(row)

    start_x, start_y = map(int, input("Enter the starting point coordinates (x y): ").split())
    start = Node(start_x, start_y)

    destination_x, destination_y = map(int, input("Enter the destination point coordinates (x y): ").split())
    destination = Node(destination_x, destination_y)

    path = bfs_traversal(grid, start, destination)

    if path:
        print("Path from start to destination:")
        for node in path:
            print(f"({node.x}, {node.y})")
    else:
        print("No path found from start to destination")

if __name__ == "__main__":
    main()
