from collections import deque

class Node:
    def __init__(self, a, b, z):
        self.x = a
        self.y = b
        self.depth = z

class DFS:
    def __init__(self):
        self.directions = 4
        self.x_move = [1, -1, 0, 0]
        self.y_move = [0, 0, 1, -1]
        self.N = 0
        self.found = False
        self.goal_level = 0
        self.state = 0
        self.source = None
        self.goal = None
        self.init()

    def init(self):
        graph = [
            [0, 0, 1, 0, 1],
            [0, 1, 1, 1, 1],
            [0, 1, 0, 0, 1],
            [1, 1, 0, 1, 1],
            [1, 0, 0, 0, 1]
        ]
        self.N = len(graph)
        source_x = 0  # source state
        source_y = 2
        goal_x = 4  # goal state
        goal_y = 4
        self.source = Node(source_x, source_y, 0)
        self.goal = Node(goal_x, goal_y, 999999)
        self.st_dfs(graph, self.source)
        if self.found:
            print("Goal found")
            print("Number of moves required =", self.goal.depth)
        else:
            print("Goal can not be reached from starting block")

    def print_direction(self, m, x, y):
        if m == 0:
            print("Moving Down", x, y)
        elif m == 1:
            print("Moving Up", x, y)
        elif m == 2:
            print("Moving Right", x, y)
        else:
            print("Moving Left", x, y)

    def st_dfs(self, graph, u):
        graph[u.x][u.y] = 0
        for j in range(self.directions):
            v_x = u.x + self.x_move[j]
            v_y = u.y + self.y_move[j]
            if 0 <= v_x < self.N and 0 <= v_y < self.N and graph[v_x][v_y] == 1:
                v_depth = u.depth + 1
                self.print_direction(j, v_x, v_y)
                if v_x == self.goal.x and v_y == self.goal.y:
                    self.found = True
                    self.goal.depth = v_depth
                    return
                child = Node(v_x, v_y, v_depth)
                self.st_dfs(graph, child)
            if self.found:
                return

def main():
    d = DFS()

if __name__ == "__main__":
    main()


# Moving Down 1 2
# Moving Right 1 3
# Moving Right 1 4
# Moving Down 2 4
# Moving Down 3 4
# Moving Down 4 4
# Goal found
# Number of moves required = 6