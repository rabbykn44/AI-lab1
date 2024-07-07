# Write a program where a robot traverses on a 2D plane using the BFS algorithm and goes from start to
# destination point. Now print the path it will traverse to reach the destination.
# (Hint: Save parent state information and use that information to write a recursive function
# for printing the path.)
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
    if destination not in parent:
        return [destination]
    return construct_path(parent, parent[destination]) + [destination]

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

# Enter the size of the grid (N x N): 5
# Enter row 1 of the grid (0 for empty, 1 for obstacle): 0 0 0 0 0
# Enter row 2 of the grid (0 for empty, 1 for obstacle): 1 0 0 1 0
# Enter row 3 of the grid (0 for empty, 1 for obstacle): 0 1 0 0 1
# Enter row 4 of the grid (0 for empty, 1 for obstacle): 0 0 0 1 1
# Enter row 5 of the grid (0 for empty, 1 for obstacle): 0 1 0 1 0
# Enter the starting point coordinates (x y): 0 0
# Enter the destination point coordinates (x y): 4 2
# Path from start to destination:
# (4, 2)