from collections import deque

class Node:
    def __init__(self, x, y, level):
        self.x = x
        self.y = y
        self.level = level

def bfs(graph, source, goal):
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    n = len(graph)
    visited = [[False] * n for _ in range(n)]
    queue = deque([source])

    while queue:
        u = queue.popleft()

        if u.x == goal.x and u.y == goal.y:
            return u.level

        for dx, dy in directions:
            v_x = u.x + dx
            v_y = u.y + dy

            if 0 <= v_x < n and 0 <= v_y < n and graph[v_x][v_y] == 1 and not visited[v_x][v_y]:
                visited[v_x][v_y] = True
                queue.append(Node(v_x, v_y, u.level + 1))

    return -1  # Goal not reachable

def main():
    n = int(input("Enter the size of the grid: "))
    print("Enter the grid (0 for obstacles and 1 for empty cells):")
    graph = [[int(x) for x in input().split()] for _ in range(n)]

    source_x, source_y = map(int, input("Enter the source point coordinates (x y): ").split())
    source = Node(source_x, source_y, 0)

    goal_x, goal_y = map(int, input("Enter the goal point coordinates (x y): ").split())
    goal = Node(goal_x, goal_y, 0)

    min_moves = bfs(graph, source, goal)

    if min_moves != -1:
        print("Goal found")
        print("Number of moves required =", min_moves)
    else:
        print("Goal cannot be reached from the starting block")

if __name__ == "__main__":
    main()

# Enter the size of the grid: 5
# Enter the grid (0 for obstacles and 1 for empty cells):
# 0 0 1 0 1
# 0 1 1 1 1
# 0 1 0 0 1
# 1 1 0 1 1
# 1 0 0 0 1
# Enter the source point coordinates (x y): 0 2
# Enter the goal point coordinates (x y): 4 4
# Goal found
# Number of moves required = 6