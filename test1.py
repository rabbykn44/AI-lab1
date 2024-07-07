class GraphColoring:
    def graphColor(self, g, noc):
        self.V = len(g)
        self.color = [0] * self.V
        self.graph = g

        try:
            self.solve(0, noc)
            print("No solution")
        except Exception as e:
            print("\nSolution exists")
            self.display()

    def solve(self, v, numOfColors):
        if v == self.V:
            raise Exception("Solution found")

        for c in range(1, numOfColors + 1):
            if self.isPossible(v, c):
                self.color[v] = c
                self.solve(v + 1, numOfColors)
                self.color[v] = 0

    def isPossible(self, v, c):
        for neighbor in self.graph[v]:
            if self.color[neighbor] == c:
                return False
        return True

    def display(self):
        textColor = ["", "RED", "GREEN", "BLUE", "YELLOW", "ORANGE", "PINK", "BLACK", "BROWN", "WHITE", "PURPLE", "VIOLET"]
        print("\nColors : ", end="")
        for i in range(self.V):
            print(textColor[self.color[i]], end=" ")
        print()


if __name__ == "__main__":
    print("Graph Coloring Algorithm Test\n")

    gc = GraphColoring()

    graph = [
        [1, 2, 3],          # New South Wales (index 0) connects to Victoria (1), Queensland (2), and South Australia (3)
        [0, 3],             # Victoria (index 1) connects to New South Wales (0) and South Australia (3)
        [0, 3, 4],          # Queensland (index 2) connects to New South Wales (0), Victoria (1), South Australia (3), and Northern Territory (4)
        [0, 1, 2, 4],    # South Australia (index 3) connects to New South Wales (0), Victoria (1), Queensland (2), Northern Territory (4), and Western Australia (5)
        [2, 3],         # Northern Territory (index 4) connects to Queensland (2), South Australia (3), and Western Australia (5)
        [ 4],              # Western Australia (index 5) connects to South Australia (3) and Northern Territory (4)
    ]

    c = int(input("Enter the number of colors: "))

    gc.graphColor(graph, c)

    
    









   