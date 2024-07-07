class IterativeDeepening:
    def __init__(self):
        self.stack = []
        self.number_of_nodes = 0
        self.depth = 0
        self.max_depth = 0
        self.goal_found = False

    def iterative_deepening(self, adjacency_matrix, destination):
        self.number_of_nodes = len(adjacency_matrix) - 1
        while not self.goal_found:
            self.depth_limited_search(adjacency_matrix, 1, destination)
            self.max_depth += 1
        print("\nGoal Found at depth", self.depth)

    def depth_limited_search(self, adjacency_matrix, source, goal):
        self.stack = [source]
        self.depth = 0
        print("\nAt Depth", self.max_depth)
        print(source, end="\t")

        visited = [0] * (self.number_of_nodes + 1)
        visited[source] = 1

        while self.stack:
            element = self.stack[-1]
            destination = 1

            while destination <= self.number_of_nodes:
                if self.depth < self.max_depth:
                    if adjacency_matrix[element][destination] == 1 and visited[destination] == 0:
                        self.stack.append(destination)
                        visited[destination] = 1
                        print(destination, end="\t")
                        self.depth += 1
                        if goal == destination:
                            self.goal_found = True
                            return
                        element = destination
                        destination = 1
                        continue
                else:
                    break
                destination += 1

            self.stack.pop()
            self.depth -= 1

if __name__ == "__main__":
    import sys

    try:
        number_of_nodes = int(input("Enter the number of nodes in the graph: "))
        adjacency_matrix = [[0] * (number_of_nodes + 1) for _ in range(number_of_nodes + 1)]

        print("Enter the adjacency matrix:")
        for i in range(1, number_of_nodes + 1):
            row = list(map(int, input().split()))
            for j in range(1, number_of_nodes + 1):
                adjacency_matrix[i][j] = row[j-1]

        destination = int(input("Enter the destination for the graph: "))

        iterative_deepening = IterativeDeepening()
        iterative_deepening.iterative_deepening(adjacency_matrix, destination)
    except ValueError:
        print("Wrong Input format")
    except Exception as e:
        print(f"An error occurred: {e}")


