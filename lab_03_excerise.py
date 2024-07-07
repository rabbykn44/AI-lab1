# Write a program to find the topological order of node traversal of the robot on the 2D graph plane.


import random
from collections import deque, defaultdict

class Node:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def print_grid(grid):
    for row in grid:
        print(" ".join(map(str, row)))

def generate_grid(N, obstacles):
    grid = [[0] * N for _ in range(N)]
    for obstacle in obstacles:
        x, y = obstacle
        grid[x][y] = 1
    return grid

def get_neighbors(x, y, N):
    neighbors = []
    if x + 1 < N:  # move down
        neighbors.append((x + 1, y))
    if y + 1 < N:  # move right
        neighbors.append((x, y + 1))
    return neighbors

def topological_sort(grid, N):
    in_degree = defaultdict(int)
    graph = defaultdict(list)
    
    # Create the graph based on movement dependencies
    for x in range(N):
        for y in range(N):
            if grid[x][y] == 0:
                for nx, ny in get_neighbors(x, y, N):
                    if grid[nx][ny] == 0:
                        graph[(x, y)].append((nx, ny))
                        in_degree[(nx, ny)] += 1

    # Find all nodes with no incoming edges
    zero_in_degree_queue = deque([(x, y) for x in range(N) for y in range(N) if grid[x][y] == 0 and in_degree[(x, y)] == 0])
    
    topological_order = []
    
    while zero_in_degree_queue:
        node = zero_in_degree_queue.popleft()
        topological_order.append(node)
        
        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                zero_in_degree_queue.append(neighbor)

    return topological_order

def main():
    N = int(input("Enter the grid size N: "))
    obstacles_count = random.randint(1, N * N // 3)
    obstacles = [(random.randint(0, N-1), random.randint(0, N-1)) for _ in range(obstacles_count)]
    grid = generate_grid(N, obstacles)
    print("Generated Grid:")
    print_grid(grid)
    
    topological_order = topological_sort(grid, N)
    
    if topological_order:
        print("Topological Order of Node Traversal:")
        for (x, y) in topological_order:
            print(f"({x}, {y})", end=" -> ")
        print("(End)")
    else:
        print("No valid topological order exists due to obstacles")

if __name__ == "__main__":
    main()

# Enter the grid size N: 5
# Generated Grid:
# 1 1 0 0 0
# 0 1 0 0 0
# 0 1 0 0 1
# 0 0 0 0 1
# 1 1 0 0 0
# Topological Order of Node Traversal:
# (0, 2) -> (1, 0) -> (1, 2) -> (0, 3) -> (2, 0) -> (2, 2) -> (1, 3) -> (0, 4) -> (3, 0) -> (2, 3) -> (1, 4) -> (3, 1) -> (3, 2) -> (4, 2) -> (3, 3) -> (4, 3) -> (4, 4) -> (End)