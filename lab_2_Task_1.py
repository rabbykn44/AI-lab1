# Write a program to perform BFS traversal on a 2D plane by taking the user input of grid size N. After
# that generate N×N matrix and place the obstacles randomly. Now print the matrix and take user input
# of starting and goal state.


import random
from collections import deque

class Node:
    def __init__(self, x, y, level):
        self.x = x
        self.y = y
        self.level = level

def generate_grid(N, obstacles):
    grid = [[0] * N for _ in range(N)]
    for _ in range(obstacles):
        x = random.randint(0, N-1)
        y = random.randint(0, N-1)
        grid[x][y] = 1
    return grid

def print_grid(grid):
    for row in grid:
        print(" ".join(map(str, row)))

def bfs_traversal(grid, source, goal):
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    n = len(grid)
    visited = [[False] * n for _ in range(n)]
    queue = deque([source])

    while queue:
        u = queue.popleft()

        if u.x == goal.x and u.y == goal.y:
            return u.level

        for dx, dy in directions:
            v_x = u.x + dx
            v_y = u.y + dy

            if 0 <= v_x < n and 0 <= v_y < n and grid[v_x][v_y] == 0 and not visited[v_x][v_y]:
                visited[v_x][v_y] = True
                queue.append(Node(v_x, v_y, u.level + 1))

    return -1  # Goal not reachable

def main():
    N = int(input("Enter the size of the grid (N x N): "))
    obstacles = int(input("Enter the number of obstacles: "))

    grid = generate_grid(N, obstacles)
    print("\nGenerated Grid:")
    print_grid(grid)

    source_x, source_y = map(int, input("\nEnter the starting state coordinates (x y): ").split())
    source = Node(source_x, source_y, 0)

    goal_x, goal_y = map(int, input("Enter the goal state coordinates (x y): ").split())
    goal = Node(goal_x, goal_y, 0)

    min_moves = bfs_traversal(grid, source, goal)

    if min_moves != -1:
        print("\nGoal found")
        print("Number of moves required =", min_moves)
    else:
        print("\nGoal cannot be reached from the starting state")

if __name__ == "__main__":
    main()

# Enter the size of the grid (N x N): 5
# Enter the number of obstacles: 8

# Generated Grid:
# 1 0 0 0 0
# 0 0 0 0 0
# 0 1 0 1 0
# 1 1 1 0 0
# 0 0 1 1 0

# Enter the starting state coordinates (x y): 0 0
# Enter the goal state coordinates (x y): 4 4

# Goal found
# Number of moves required = 8