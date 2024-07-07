# Write a program to perform DFS traversal on a 2D plane by taking the user input of grid size N. After
# that generate N×N matrix and place the obstacles randomly. Now print the matrix and take user input
# of starting and goal state.

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

def dfs(grid, start, goal):
    stack = [(start, 0)]
    visited = set()
    while stack:
        current, depth = stack.pop()
        visited.add((current.x, current.y))
        if current.x == goal.x and current.y == goal.y:
            return depth
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nx, ny = current.x + dx, current.y + dy
            if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and grid[nx][ny] == 0 and (nx, ny) not in visited:
                stack.append((Node(nx, ny), depth + 1))
    return -1

def main():
    N = int(input("Enter the grid size N: "))
    obstacles_count = random.randint(1, N*N // 3)
    obstacles = [(random.randint(0, N-1), random.randint(0, N-1)) for _ in range(obstacles_count)]
    grid = generate_grid(N, obstacles)
    print("Generated Grid:")
    print_grid(grid)
    start_x, start_y = map(int, input("Enter starting state coordinates (x y): ").split())
    goal_x, goal_y = map(int, input("Enter goal state coordinates (x y): ").split())
    start = Node(start_x, start_y)
    goal = Node(goal_x, goal_y)
    depth = dfs(grid, start, goal)
    if depth != -1:
        print("Goal found at depth:", depth)
    else:
        print("Goal cannot be reached from the starting state")

if __name__ == "__main__":
    main()
# Enter the grid size N: 5
# Generated Grid:
# 0 0 0 0 0
# 0 0 0 0 0
# 0 0 0 0 0
# 0 0 0 0 0
# 0 1 0 0 0
# Enter starting state coordinates (x y): 0 0
# Enter goal state coordinat