

def graph_coloring(adj_list, num_of_colors):
    colors = {}

    def solve(v):
        if v not in adj_list:
            raise Exception("Solution found")
        for c in range(1, num_of_colors + 1):
            if is_possible(v, c):
                colors[v] = c
                solve(next_node(v))
                colors[v] = 0

    def is_possible(v, c):
        for neighbor in adj_list[v]:
            if colors.get(neighbor) == c:
                return False
        return True

    def next_node(v):
        for node in adj_list:
            if node not in colors:
                return node
        return None

    def display():
        text_color = ["", "RED", "GREEN", "BLUE", "YELLOW", "ORANGE", "PINK",
                      "BLACK", "BROWN", "WHITE", "PURPLE", "VIOLET"]
        print("Colors:")
        for node, color_index in colors.items():
            print(f"{node}: {text_color[color_index]}")

    try:
        solve(next(iter(adj_list)))
        print("No solution")
    except Exception as e:
        print("\nSolution exists")
        display()


print("Graph Coloring Algorithm Test")

adj_list = {
    "WA": ["NT", "SA"],
    "NT": ["WA", "SA", "Q"],
    "SA": ["WA", "NT", "Q", "NSW", "V"],
    "Q": ["NT", "SA", "NSW"],
    "NSW": ["SA", "Q", "V"],
    "V": ["SA", "NSW"],
    "T": []
}


num_colors = int(input("\nEnter number of colors: "))

graph_coloring(adj_list, num_colors)


# Graph Coloring Algorithm Test

# Enter number of colors: 3

# Solution exists
# Colors:
# WA: RED
# NT: GREEN
# SA: BLUE
# Q: RED
# NSW: GREEN
# V: RED
# T: RED