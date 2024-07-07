# Write a program to find the path from source to destination using DFS.

import random

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

def dfs(grid, current, goal, path, visited):
    if current.x == goal.x and current.y == goal.y:
        path.append((current.x, current.y))
        return True
    
    visited.add((current.x, current.y))
    path.append((current.x, current.y))
    
    for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        nx, ny = current.x + dx, current.y + dy
        
        if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and grid[nx][ny] == 0 and (nx, ny) not in visited:
            if dfs(grid, Node(nx, ny), goal, path, visited):
                return True

    path.pop()
    return False

def find_path(grid, start, goal):
    path = []
    visited = set()
    if dfs(grid, start, goal, path, visited):
        return path
    return []

def main():
    N = int(input("Enter the grid size N: "))
    obstacles_count = random.randint(1, N * N // 3)
    obstacles = [(random.randint(0, N-1), random.randint(0, N-1)) for _ in range(obstacles_count)]
    grid = generate_grid(N, obstacles)
    print("Generated Grid:")
    print_grid(grid)
    
    start_x, start_y = map(int, input("Enter starting state coordinates (x y): ").split())
    goal_x, goal_y = map(int, input("Enter goal state coordinates (x y): ").split())
    
    start = Node(start_x, start_y)
    goal = Node(goal_x, goal_y)
    
    path = find_path(grid, start, goal)
    
    if path:
        print("Path from source to destination:")
        for (x, y) in path:
            print(f"({x}, {y})", end=" -> ")
        print("(Goal)")
    else:
        print("No path found from source to destination")

if __name__ == "__main__":
    main()
